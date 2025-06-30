# 📦 Import library yang dibutuhkan
import pandas as pd
from datetime import datetime, timedelta, time
from collections import defaultdict
import re
import os
import sys
from openpyxl.styles import PatternFill  # Untuk menulis ke Excel dengan style (opsional)

print("\n🚀 Starting main course scheduling process...")

# 📁 Nama file Excel dan nama sheet yang digunakan
EXCEL_FILE = "Data_Dosen_NSP.xlsx"
SHEET_NAME = "Sheet1"

# ❗ Cek apakah file Excel tersedia
if not os.path.exists(EXCEL_FILE):
    print(f"❌ File '{EXCEL_FILE}' tidak ditemukan di folder ini: {os.getcwd()}")
    sys.exit(1)

# ✅ Baca data dari file Excel
try:
    scheduled_items_df = pd.read_excel(EXCEL_FILE, sheet_name=SHEET_NAME)
except Exception as e:
    print(f"❌ Gagal membaca sheet '{SHEET_NAME}': {e}")
    sys.exit(1)

# 🔠 Normalisasi nama kolom agar huruf besar semua
scheduled_items_df.columns = scheduled_items_df.columns.str.strip().str.upper()

# 📆 Daftar hari perkuliahan dan waktu istirahat
WEEK_DAYS = ["SENIN", "SELASA", "RABU", "KAMIS", "JUMAT"]
BREAK_PERIODS = [(time(12, 0), time(13, 0)), (time(18, 0), time(18, 30))]

# 🏫 Daftar ruangan kampus berdasarkan gedung dan lantai
CAMPUS_ROOMS = {
    'BUILDING A': {
        2: [f"A2-{i}" for i in range(1, 9)],
        3: [f"A3-{i}" for i in range(1, 9)],
        4: [f"A4-{i}" for i in range(1, 9)],
        5: [f"A5-{i}" for i in range(1, 9)],
    },
    'BUILDING B': {
        3: [f"B3-{i}" for i in range(1, 6)],
        4: [f"B4-{i}" for i in range(1, 6)],
        5: [f"B5-{i}" for i in range(1, 6)],
    }
}

# 🧑‍🏫 Preferensi lantai berdasarkan departemen
DEPARTMENT_FLOOR_PREFS = {
    'TI': {'preferred_floors': [3, 4]}, 'SI': {'preferred_floors': [3, 4]},
    'DK': {'preferred_floors': [4, 5]}, 'SD': {'preferred_floors': [2, 3]},
    'HK': {'preferred_floors': [3, 4]}, 'ME': {'preferred_floors': [4, 5]},
    'EL': {'preferred_floors': [4, 5]}, 'AKT': {'preferred_floors': [2, 3]},
    'MJN': {'preferred_floors': [2, 3]},
}

# 🔧 Membersihkan dan mengisi data yang kosong
scheduled_items_df["AVAILABLE DAY"] = scheduled_items_df["AVAILABLE DAY"].fillna("ALL").str.upper()
scheduled_items_df["AVAILABLE TIME"] = scheduled_items_df["AVAILABLE TIME"].fillna("ALL").astype(str).str.upper()
scheduled_items_df["KELAS"] = scheduled_items_df["KELAS"].astype(str).str.upper()
scheduled_items_df["PRIORITAS"] = scheduled_items_df["PRIORITAS"].fillna(4).astype(int)
scheduled_items_df["SKS"] = scheduled_items_df["SKS"].astype(int)

# 🧠 Fungsi bantu

# Hitung durasi kuliah dari SKS (1 SKS = 50 menit)
def calculate_lecture_duration(sks_credits):
    return timedelta(minutes=50 * sks_credits)

# Cek apakah kelas malam (jika mengandung huruf M)
def is_night_class(course_class):
    return "M" in course_class

# Atur waktu perkuliahan berdasarkan jenis kelas
def get_class_time_window(course_class):
    return (time(17, 0), time(22, 0)) if is_night_class(course_class) else (time(8, 0), time(18, 0))

# Buat slot waktu setiap 10 menit
def generate_time_slots(start, end, interval=10):
    slots = []
    now = datetime.combine(datetime.today(), start)
    end_dt = datetime.combine(datetime.today(), end)
    while now < end_dt:
        slots.append(now.time())
        now += timedelta(minutes=interval)
    return slots

# Cek apakah waktu kuliah menabrak jam istirahat
def check_break_overlap(start, end):
    return any(start < b_end and end > b_start for b_start, b_end in BREAK_PERIODS)

# Cek apakah ada konflik dengan jadwal yang sudah ada
def check_conflict(schedule, day, key, start, end):
    return any(not (end <= s or start >= e) for s, e in schedule[day][key])

# Cari ruangan yang sesuai berdasarkan preferensi jurusan
def find_room(day, start, end, course_class, schedule):
    match = re.match(r"([A-Z]{2})", course_class)
    code = match.group(1) if match else None
    floors = DEPARTMENT_FLOOR_PREFS.get(code, {}).get("preferred_floors", [])
    for building, maps in CAMPUS_ROOMS.items():
        for floor in floors:
            for room in maps.get(floor, []):
                if not check_conflict(schedule, day, room, start, end):
                    return room
    return None

# Cari slot waktu yang memungkinkan (tidak bentrok dan sesuai jam dosen)
def find_slot(day, course_class, lecturer, duration, available_times, schedule):
    start_win, end_win = get_class_time_window(course_class)
    for start in generate_time_slots(start_win, end_win):
        end = (datetime.combine(datetime.today(), start) + duration).time()
        if end > end_win or check_break_overlap(start, end):
            continue
        if available_times != "ALL":
            try:
                allowed_start = datetime.strptime(available_times.split("-")[0].strip(), "%H:%M").time()
                if start < allowed_start:
                    continue
            except:
                pass
        if check_conflict(schedule, day, lecturer, start, end):
            continue
        if check_conflict(schedule, day, course_class, start, end):
            continue
        return start, end
    return None, None

# 💡 Variabel penyimpan hasil akhir
final_schedule = []
unassigned = []
occupancy = defaultdict(lambda: defaultdict(list))  # Penyimpanan jadwal sementara
sorted_df = scheduled_items_df.sort_values("PRIORITAS")  # Urutkan berdasarkan prioritas

# 🔁 Proses utama penjadwalan
for _, row in sorted_df.iterrows():
    lecturer = row["DOSEN"]
    course = row["MATA KULIAH"]
    sks = row["SKS"]
    classes = row["KELAS"]
    available_days = WEEK_DAYS if row["AVAILABLE DAY"] == "ALL" else [d.strip().upper() for d in row["AVAILABLE DAY"].split(",")]
    available_times = row["AVAILABLE TIME"]
    duration = calculate_lecture_duration(sks)

    for cls in classes.split(","):
        cls = cls.strip()
        if not cls:
            continue
        scheduled = False
        for day in available_days:
            day = day.strip().upper()
            if day not in WEEK_DAYS:
                continue
            start, end = find_slot(day, cls, lecturer, duration, available_times, occupancy)
            if start and end:
                room = find_room(day, start, end, cls, occupancy)
                if not room:
                    continue
                status = "ONLINE" if end > time(21, 0) else "SCHEDULED"
                final_schedule.append({
                    "Lecturer": lecturer,
                    "Course Title": course,
                    "Course Class": cls,
                    "SKS": sks,
                    "Day": day,
                    "Time": f"{start.strftime('%H:%M')} - {end.strftime('%H:%M')}",
                    "Room": room,
                    "Status": status
                })
                # Simpan jadwal ke memori (untuk pengecekan bentrok)
                occupancy[day][lecturer].append((start, end))
                occupancy[day][cls].append((start, end))
                occupancy[day][room].append((start, end))
                scheduled = True
                break
        if not scheduled:
            # Jika tidak ada slot tersedia, jadikan ONLINE
            default_start = get_class_time_window(cls)[0]
            default_end = (datetime.combine(datetime.today(), default_start) + duration).time()
            final_schedule.append({
                "Lecturer": lecturer,
                "Course Title": course,
                "Course Class": cls,
                "SKS": sks,
                "Day": "ONLINE",
                "Time": f"{default_start.strftime('%H:%M')} - {default_end.strftime('%H:%M')}",
                "Room": "-",
                "Status": "ONLINE"
            })
            unassigned.append({
                "Lecturer": lecturer,
                "Course Title": course,
                "Course Class": cls,
                "Reason": "No available slot found",
                "Available Day": ", ".join(available_days),
                "Available Times": available_times,
                "SKS": sks
            })

# 💾 Simpan hasil jadwal ke file Excel
df_out = pd.DataFrame(final_schedule)
df_un = pd.DataFrame(unassigned)
output_file = f"scheduled_courses_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"
with pd.ExcelWriter(output_file, engine="openpyxl") as writer:
    df_out.to_excel(writer, sheet_name="SCHEDULE", index=False)
    df_un.to_excel(writer, sheet_name="UNSCHEDULED_REPORT", index=False)

print(f"✅ Jadwal berhasil disimpan ke: {output_file}")