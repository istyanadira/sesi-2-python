import pandas as pd
import os

# --- Nama File Excel Utama ---
MASTER_EXCEL_FILE = "Mapping Jadwal Mengajar Prodi Teknik Informatika.xlsx"

# --- Fungsi untuk Memuat Data ---
def load_data():
    """Memuat semua data dari sheet yang relevan di file Excel."""
    data = {}
    try:
        # Membaca sheet 'Mapping mata kuliah'
        # skiprows=2 karena ada 2 baris header yang tidak relevan di awal (berdasarkan analisis sebelumnya)
        data['mapping_mata_kuliah'] = pd.read_excel(MASTER_EXCEL_FILE, sheet_name='Mapping mata kuliah', skiprows=2)
        
        # Membaca sheet 'angkatan 2024'
        # skiprows=3 karena ada 3 baris header yang tidak relevan di awal
        data['angkatan_2024'] = pd.read_excel(MASTER_EXCEL_FILE, sheet_name='angkatan 2024', skiprows=3)
        data['angkatan_2023'] = pd.read_excel(MASTER_EXCEL_FILE, sheet_name='angkatan 2023', skiprows=3)
        data['angkatan_2022'] = pd.read_excel(MASTER_EXCEL_FILE, sheet_name='angkatan 2022', skiprows=3)
        
        # Membaca sheet 'Pembimbing Akademik 2024'
        # skiprows=2
        data['pembimbing_akademik_2024'] = pd.read_excel(MASTER_EXCEL_FILE, sheet_name='Pembimbing Akademik 2024', skiprows=2)

        # Inisialisasi DataFrame kosong untuk jadwal utama
        data['jadwal_sekarang'] = pd.DataFrame(columns=[
            'Kode Mata Kuliah', 'Nama Mata Kuliah', 'SKS', 'Semester', 'Kelas',
            'Hari', 'Jam Mulai', 'Jam Selesai', 'Ruangan', 'Dosen Pengampu'
        ])
        
        print("Data berhasil dimuat dari Excel.")
    except FileNotFoundError:
        print(f"Error: File Excel '{MASTER_EXCEL_FILE}' tidak ditemukan. Pastikan file berada di direktori yang sama.")
        exit()
    except KeyError as e:
        print(f"Error: Sheet '{e}' tidak ditemukan dalam file Excel. Pastikan nama sheet benar.")
        exit()
    except Exception as e:
        print(f"Terjadi kesalahan saat memuat data dari Excel: {e}")
        exit()
    return data

# --- Global variable untuk menyimpan jadwal ---
data_aplikasi = {} # Akan diisi saat load_data dipanggil

# --- Fungsi-fungsi Operasi Jadwal (tetap sama seperti sebelumnya) ---
# ... (tampilkan_jadwal_saat_ini, tambah_jadwal_baru, hapus_jadwal, ubah_jadwal) ...

def ekspor_jadwal_ke_excel(jadwal):
    """Mengekspor jadwal perkuliahan ke file Excel."""
    if jadwal.empty:
        print("\nTidak ada jadwal untuk diekspor.")
        input("Tekan Enter untuk melanjutkan...")
        return
        
    file_name = input("Masukkan nama file Excel untuk disimpan (misal: jadwal_perkuliahan_output.xlsx): ").strip()
    if not file_name.lower().endswith(".xlsx"):
        file_name += ".xlsx"

    try:
        # Menggunakan to_excel untuk menyimpan ke file Excel
        jadwal.to_excel(file_name, index=False)
        print(f"Jadwal berhasil diekspor ke '{file_name}'")
    except Exception as e:
        print(f"Terjadi kesalahan saat mengekspor jadwal: {e}")
    input("Tekan Enter untuk melanjutkan...")

# --- Main Program / Menu (tetap sama seperti sebelumnya) ---
def main():
    global data_aplikasi
    data_aplikasi = load_data() 

    while True:
        os.system('cls' if os.name == 'nt' else 'clear') 
        print("===================================================")
        print("   Generate Jadwal Perkuliahan                     ")
        print("   Universitas Nusa Putra University               ")
        print("===================================================")
        print("1. Tampilkan Jadwal saat ini")
        print("2. Tambah Jadwal baru")
        print("3. Hapus Jadwal")
        print("4. Ubah Jadwal")
        print("5. Ekspor Jadwal ke Excel")
        print("6. Keluar Aplikasi")
        print("===================================================")

        pilihan = input("Masukkan pilihan Anda (1-6): ").strip()

        if pilihan == '1':
            tampilkan_jadwal_saat_ini(data_aplikasi['jadwal_sekarang'])
        elif pilihan == '2':
            data_aplikasi['jadwal_sekarang'] = tambah_jadwal_baru(data_aplikasi['jadwal_sekarang'], data_aplikasi['mapping_mata_kuliah'])
        elif pilihan == '3':
            data_aplikasi['jadwal_sekarang'] = hapus_jadwal(data_aplikasi['jadwal_sekarang'])
        elif pilihan == '4':
            data_aplikasi['jadwal_sekarang'] = ubah_jadwal(data_aplikasi['jadwal_sekarang'], data_aplikasi['mapping_mata_kuliah'])
        elif pilihan == '5':
            ekspor_jadwal_ke_excel(data_aplikasi['jadwal_sekarang'])
        elif pilihan == '6':
            print("Terima kasih telah menggunakan aplikasi penjadwalan. Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid. Mohon masukkan angka antara 1 dan 6.")
            input("Tekan Enter untuk melanjutkan...")

if __name__ == "__main__":
    main()