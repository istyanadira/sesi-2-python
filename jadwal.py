import pandas as pd
from tabulate import tabulate
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# --- KONFIGURASI DAN DATA PRE-DEFINED ---

AVAILABLE_ROOMS = {
    'RKT 1': [1, 2, 3],
    'RKT 2': [4, 5, 6],
    'RKT 3': [3, 4, 5]
}

ROOM_PREFERENCES = {
    'TI': {'floors': [3, 4], 'text': 'disarankan memilih ruangan di lantai 4 atau 3'},
    'SI': {'floors': [3, 4], 'text': 'disarankan memilih ruangan di lantai 4 atau 3'},
    'DKV': {'floors': [5], 'text': 'disarankan memilih ruangan di lantai 5'}
}

ALLOWED_DAYS = ['SENIN', 'JUMAT']
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
        print("Error: Waktu di luar batas yang diizinkan.")
        return False

    for break_start, break_end in BREAKS:
        if max(start_t, break_start) < min(end_t, break_end):
            print(f"Error: Waktu bertabrakan dengan jam istirahat {break_start} - {break_end}.")
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
            return False
    return True

# --- FITUR TAMBAHAN ---

def cek_ketersediaan(df):
    print("\n--- Cek Ketersediaan Ruangan ---")
    hari = input(f"Hari ({'/'.join(ALLOWED_DAYS)}): ").upper()
    if hari not in ALLOWED_DAYS:
        print("Hari tidak valid.")
        return

    mulai = input("Jam mulai (HH:MM): ")
    selesai = input("Jam selesai (HH:MM): ")
    if not is_time_slot_valid(mulai, selesai):
        return

    print("\nRuangan yang tersedia:")
    for gedung, lantai_list in AVAILABLE_ROOMS.items():
        for lantai in lantai_list:
            if is_room_available(df, hari, mulai, selesai, gedung, lantai):
                print(f"- {gedung} Lantai {lantai}")

# Visualisasi Jadwal Mingguan

def visualisasi_jadwal(df):
    if df.empty:
        print("\nJadwal kosong.")
        return

    df['MULAI_NUM'] = pd.to_datetime(df['MULAI'], format='%H:%M').dt.hour + pd.to_datetime(df['MULAI'], format='%H:%M').dt.minute / 60
    df['SELESAI_NUM'] = pd.to_datetime(df['SELESAI'], format='%H:%M').dt.hour + pd.to_datetime(df['SELESAI'], format='%H:%M').dt.minute / 60

    fig, ax = plt.subplots(figsize=(12, 6))
    colors = plt.cm.get_cmap('tab10', len(df['HARI'].unique()))
    hari_order = ['SENIN', 'JUMAT']

    for i, (_, row) in enumerate(df.iterrows()):
        y_pos = hari_order.index(row['HARI'])
        ax.barh(y_pos, row['SELESAI_NUM'] - row['MULAI_NUM'], left=row['MULAI_NUM'], color=colors(y_pos), edgecolor='black')
        ax.text(row['MULAI_NUM'] + 0.1, y_pos, f"{row['DOSEN']} ({row['KELAS']})", va='center', fontsize=8)

    ax.set_yticks(range(len(hari_order)))
    ax.set_yticklabels(hari_order)
    ax.set_xlim(8, 20)
    ax.set_xlabel('Jam')
    ax.set_title('Visualisasi Jadwal Mingguan')
    plt.grid(True, axis='x', linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.show()

# --- MAIN MENU UTAMA ---

def main():
    nama_file = 'reservasi_ruangan.xlsx'
    try:
        df = pd.read_excel(nama_file)
    except:
        df = pd.DataFrame(columns=['HARI', 'DOSEN', 'MATAKULIAH', 'KELAS', 'PRODI', 'GEDUNG', 'LANTAI', 'MULAI', 'SELESAI'])

    while True:
        print("\n===== MENU UTAMA =====")
        print("1. Tampilkan Jadwal")
        print("2. Tambah Reservasi")
        print("3. Hapus Reservasi")
        print("4. Cek Ketersediaan Ruangan")
        print("5. Visualisasi Jadwal")
        print("6. Simpan & Keluar")
        pilihan = input("Pilih opsi (1-6): ")

        if pilihan == '1':
            if df.empty:
                print("\nBelum ada reservasi.")
            else:
                print(tabulate(df, headers='keys', tablefmt='grid', showindex=True))

        elif pilihan == '2':
            data = input("Masukkan data (Dosen - Matkul - Kelas): ")
            try:
                dosen, matkul, kelas = [x.strip() for x in data.split('-')]
                prodi = kelas[:2].upper()
                hari = input("Hari: ").upper()
                mulai = input("Jam Mulai (HH:MM): ")
                selesai = input("Jam Selesai (HH:MM): ")
                gedung = input("Gedung: ").upper()
                lantai = int(input("Lantai: "))
                if not is_time_slot_valid(mulai, selesai): continue
                if gedung not in AVAILABLE_ROOMS or lantai not in AVAILABLE_ROOMS[gedung]:
                    print("Gedung/lantai tidak tersedia.")
                    continue
                if is_room_available(df, hari, mulai, selesai, gedung, lantai):
                    df = pd.concat([df, pd.DataFrame.from_records([{
                        'HARI': hari, 'DOSEN': dosen, 'MATAKULIAH': matkul,
                        'KELAS': kelas, 'PRODI': prodi, 'GEDUNG': gedung,
                        'LANTAI': lantai, 'MULAI': mulai, 'SELESAI': selesai
                    }])], ignore_index=True)
                    print("Reservasi berhasil ditambahkan!")
                else:
                    print("Ruangan tidak tersedia.")
            except Exception as e:
                print("Format input salah.", e)

        elif pilihan == '3':
            print(tabulate(df, headers='keys', tablefmt='grid', showindex=True))
            try:
                idx = int(input("Index yang ingin dihapus: "))
                df = df.drop(index=idx).reset_index(drop=True)
                print("Data dihapus.")
            except:
                print("Index tidak valid.")

        elif pilihan == '4':
            cek_ketersediaan(df)

        elif pilihan == '5':
            visualisasi_jadwal(df)

        elif pilihan == '6':
            df.to_excel(nama_file, index=False)
            print("Data disimpan. Keluar.")
            break

if __name__ == "__main__":
    main()