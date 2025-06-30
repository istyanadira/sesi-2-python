
import pandas as pd
from tabulate import tabulate
from datetime import datetime

# --- KONFIGURASI DAN DATA PRE-DEFINED ---

# 1. Daftar ruangan yang tersedia (Gedung dan daftar lantainya)
AVAILABLE_ROOMS = {
    'RKT 1': [1, 2, 3],
    'RKT 2': [4, 5, 6],
    'RKT 3': [3, 4, 5]
}

# 2. Preferensi lantai berdasarkan jurusan (PRODI)
ROOM_PREFERENCES = {
    'TI': {'floors': [3, 4], 'text': 'disarankan memilih ruangan di lantai 4 atau 3'},
    'SI': {'floors': [3, 4], 'text': 'disarankan memilih ruangan di lantai 4 atau 3'},
    'DKV': {'floors': [5], 'text': 'disarankan memilih ruangan di lantai 5'}
}

# 3. Aturan waktu reservasi
ALLOWED_DAYS = ['SENIN', 'SELASA', 'RABU', 'KAMIS', 'JUMAT']
MIN_TIME = datetime.strptime("08:00", "%H:%M").time()
MAX_TIME = datetime.strptime("20:00", "%H:%M").time()
BREAKS = [
    (datetime.strptime("12:00", "%H:%M").time(), datetime.strptime("13:00", "%H:%M").time()),
    (datetime.strptime("18:00", "%H:%M").time(), datetime.strptime("19:00", "%H:%M").time())
]

# --- FUNGSI VALIDASI ---

def is_time_slot_valid(start_str, end_str):
    try:
        start_t = datetime.strptime(start_str, "%H:%M").time()
        end_t = datetime.strptime(end_str, "%H:%M").time()
    except ValueError:
        print("Format waktu salah. Gunakan format HH:MM.")
        return False

    if not (MIN_TIME <= start_t < MAX_TIME and MIN_TIME < end_t <= MAX_TIME and start_t < end_t):
        print(f"Error: Waktu reservasi harus antara {MIN_TIME.strftime('%H:%M')} dan {MAX_TIME.strftime('%H:%M')}.")
        return False

    for break_start, break_end in BREAKS:
        if max(start_t, break_start) < min(end_t, break_end):
            print(f"Error: Tidak boleh melakukan reservasi saat jam istirahat ({break_start.strftime('%H:%M')} - {break_end.strftime('%H:%M')}).")
            return False
    return True

def is_room_available(df, day, start_str, end_str, gedung, lantai):
    start_t = datetime.strptime(start_str, "%H:%M").time()
    end_t = datetime.strptime(end_str, "%H:%M").time()

    bookings = df[(df['HARI'] == day) & (df['GEDUNG'] == gedung) & (df['LANTAI'] == lantai)]

    for _, row in bookings.iterrows():
        booked_start = datetime.strptime(row['MULAI'], "%H:%M").time()
        booked_end = datetime.strptime(row['SELESAI'], "%H:%M").time()
        if max(start_t, booked_start) < min(end_t, booked_end):
            print(f"Error: Ruangan sudah dipesan {row['MULAI']} - {row['SELESAI']} oleh {row['DOSEN']} ({row['MATAKULIAH']})")
            return False
    return True

# --- FUNGSI UTAMA ---

def muat_data(nama_file):
    kolom = ['HARI', 'DOSEN', 'MATAKULIAH', 'KELAS', 'PRODI', 'GEDUNG', 'LANTAI', 'MULAI', 'SELESAI']
    try:
        df = pd.read_excel(nama_file)
    except FileNotFoundError:
        print(f"File '{nama_file}' tidak ditemukan. Membuat baru.")
        df = pd.DataFrame(columns=kolom)
    return df

def tampilkan_jadwal(df):
    if df.empty:
        print("\nJadwal masih kosong.")
    else:
        df_sorted = df.copy()
        df_sorted['MULAI_TIME'] = pd.to_datetime(df_sorted['MULAI'], format='%H:%M').dt.time
        df_sorted = df_sorted.sort_values(by=['HARI', 'MULAI_TIME']).drop(columns=['MULAI_TIME'])
        for hari, grup in df_sorted.groupby('HARI'):
            print(f"\n----- {hari.upper()} -----")
            print(tabulate(grup, headers='keys', tablefmt='plain', showindex=False))

def tambah_reservasi(df):
    print("\n--- Tambah Reservasi Baru ---")
    data_str = input("Masukkan data (Dosen - Matkul - Kelas): ")
    parts = [p.strip() for p in data_str.split('-')]
    if len(parts) != 3:
        print("Format salah.")
        return df
    dosen, matakuliah, kelas = parts
    prodi = kelas[:2].upper()
    print(f"Prodi terdeteksi: {prodi}")

    rutin = input("Apakah ingin reservasi 3x seminggu (Senin/Rabu/Jumat)? (y/n): ").lower()

    if rutin == 'y':
        hari_list = ['SENIN', 'RABU', 'JUMAT']
    else:
        hari_list = [input("Hari (Senin-Jumat): ").strip().upper()]
        if hari_list[0] not in ALLOWED_DAYS:
            print("Hari tidak diizinkan.")
            return df

    mulai = input("Jam Mulai (HH:MM): ")
    selesai = input("Jam Selesai (HH:MM): ")
    if not is_time_slot_valid(mulai, selesai):
        return df

    print(tabulate(AVAILABLE_ROOMS.items(), headers=['Gedung', 'Lantai Tersedia'], tablefmt='grid'))
    gedung = input("Pilih Gedung: ").upper()
    try:
        lantai = int(input("Pilih Lantai: "))
    except ValueError:
        print("Lantai harus angka.")
        return df

    if gedung not in AVAILABLE_ROOMS or lantai not in AVAILABLE_ROOMS[gedung]:
        print("Gedung/lantai tidak tersedia.")
        return df

    if prodi in ROOM_PREFERENCES:
        if lantai not in ROOM_PREFERENCES[prodi]['floors']:
            print(f"Saran: {ROOM_PREFERENCES[prodi]['text']}")

    for hari in hari_list:
        if is_room_available(df, hari, mulai, selesai, gedung, lantai):
            df = pd.concat([df, pd.DataFrame([{
                'HARI': hari, 'DOSEN': dosen, 'MATAKULIAH': matakuliah, 'KELAS': kelas,
                'PRODI': prodi, 'GEDUNG': gedung, 'LANTAI': lantai, 'MULAI': mulai, 'SELESAI': selesai
            }])], ignore_index=True)
            print(f"Reservasi berhasil ditambahkan untuk hari {hari}")
        else:
            print(f"Gagal tambah untuk hari {hari} karena bentrok.")
    return df

def hapus_reservasi(df):
    if df.empty:
        print("Jadwal kosong.")
        return df
    print(tabulate(df, headers='keys', tablefmt='grid', showindex=True))
    try:
        idx = int(input("Index yang ingin dihapus: "))
        if idx in df.index:
            df = df.drop(idx).reset_index(drop=True)
            print("Reservasi berhasil dihapus.")
        else:
            print("Index tidak ditemukan.")
    except ValueError:
        pass
    return df

def main():
    nama_file = 'reservasi_ruangan.xlsx'
    df_jadwal = muat_data(nama_file)

    while True:
        print("\n===== SISTEM RESERVASI RUANGAN =====")
        print("1. Tampilkan Reservasi")
        print("2. Tambah Reservasi")
        print("3. Hapus Reservasi")
        print("4. Simpan dan Keluar")
        pilihan = input("Pilih opsi (1-4): ")

        if pilihan == '1':
            tampilkan_jadwal(df_jadwal)
        elif pilihan == '2':
            df_jadwal = tambah_reservasi(df_jadwal)
        elif pilihan == '3':
            df_jadwal = hapus_reservasi(df_jadwal)
        elif pilihan == '4':
            df_jadwal.to_excel(nama_file, index=False)
            print("Data disimpan. Keluar.")
            break
        else:
            print("Opsi tidak valid.")

if __name__ == "__main__":
    main()