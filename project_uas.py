import pandas as pd
from io import StringIO

# --- 1. Load Data ---
# Isi file dari data yang udah ada sebelumnya
file_contents = {
    "Mapping Jadwal Mengajar Prodi Teknik Informatika.xlsx - Mapping mata kuliah.csv": """Mapping Mata Kuliah Semester Ganjil TA. 2024-2025 Prodi Teknik Informatika,,,,,,,
,,,,,,,
No,Nama Dosen,Mata Kuliah,Semester,SKS,Kelas,Hari,Jam
1,"Alun Sujjada, ST., M.Kom",Algoritma dan Struktur Data,1,4,TI24A,Jumat,08.00 - 11.20
,,,,,TI24M,Rabu,18.30 - 20.30
,,Pemrograman Berbasis Platform,3,3,TI23H,Kamis,08.00 - 10.30
,,,,,TI23I,Jumat,13.00 - 15.30
,,,,,TI23T,Kamis,10.30 - 13.00
,,Kompleksitas Algoritma,3,2,TI23G,Rabu,10.30 - 12.10
,,,,,TI23J,Rabu,13.00 - 14.40
,,Pengolahan Citra Digital,5,3,TI22A,Kamis,16.00 - 18.30
,,,,,TI22E,Rabu,16.00 - 18.30
,,,,,TI22J,Jumat,16.00 - 18.30
,,Pemrograman Berbasis web,5,2,TI22M,Kamis,19.00 - 20.00
2,"Anggun Fergina, M.kom",Jaringan Komputer dan Keamanan Informasi,3,4,TI23E,Jumat,13.00 - 16.20
,,,,,TI23F,Jumat,08.00 - 11.20
,,Sistem Paralel dan Terdistribusi,3,2,TI23I,Selasa,13.00 - 14.40
,,,,,TI23T,Jumat,16.30 - 18.10
,,Rekayasa Perangkat Lunak,3,3,TI23J,Selasa,16.00 - 18.30
,,,,,TI23M,Rabu,18.30 - 20.00
,,Basis Data,3,3,TI22J,Rabu,08.00 - 10.30
,,,,,TI22T,Rabu,13.00 - 15.30
,,Projek Perangkat Lunak,5,3,TI22A,Kamis,13.00 - 15.30
,,,,,TI22E,Kamis,10.30 - 13.00
,,,,,TI22I,Kamis,08.00 - 10.30
,,Pemrograman Berbasis Web,5,2,TI22F,Rabu,16.00 - 17.40
,,,,,TI22H,Kamis,16.00 -17.40
3,"Gina Purnama Insany, S.Si.T., M.Kom",Logika Informatika,1,3,TI24A,Rabu,16.00 - 18.30
,,,,,TI24E,Rabu,10.30 - 13.00
,,,,,TI24F,Jumat,13.00 - 15.30
,,,,,TI24G,Rabu,08.00 - 10.30
,,Statistika dan Probabilitas,1,3,TI24H,Kamis,10.30 - 13.00
,,Metodologi Penelitian,5,3,TI22B,Sabtu,online
,,,,,TI22F,Jumat,16.00 - 18.30
,,,,,TI22J,Selasa,16.00 - 18.30
,,,,,TI22M,Selasa,18.30 - 20.00
,,,,,TI22T,Kamis,16.00 - 18.30
,,Data Science,5,2,TI22A,Kamis,08.00 -09.40
,,,,,TI22E,Kamis,13.00 - 14.40
,,,,,TI22C,Minggu,11.00 - 12.00
4,"Ir. Somantri, ST.,M.Kom",Jaringan Komputer dan Keamanan Informasi,3,4,TI23T,Rabu,08.00 - 11.20
,,,,,TI23I,Rabu,13.00 - 16.20
,,Metodologi Penelitian,5,3,TI22C,Minggu,14.00 - 15.30
,,,,,TI22I,Jumat,13.00 - 15.30
,,Cyber Security,5,2,TI22B,Sabtu,16.00 - 17.00
,,,,,TI22J,Kamis,08.00 - 09.40
,,,,,TI22T,Kamis,10.30 - 12.10
,,Sistem Informasi Geografis,5,2,TI22M,Rabu,18.30 - 19.30
,,Big Data arsitektur dan Infrastruktur,5,2,TI22B,Sabtu,17.00 - 18.00
,,,,,TI22J,Selasa,10.30 - 12.10
5,"Ivana Lucia Kharisma, M.Kom",Logika Informatika,1,3,TI24I,Senin,13.00 - 15.30
,,,,,TI24T,Kamis,13.00 - 15.30
,,Interaksi manusia dan Komputer,3,2,TI23A,Senin,16.00 - 17.40
,,,,,TI23F,Rabu,13.00 - 14.40
,,,,,TI23H,Rabu,16.00 - 17.40
,,,,,TI23I,Senin,10.30 - 12.10
,,Computer Vision,5,2,TI22A,Kamis,10.30 - 12.10
,,,,,TI22I,Senin,08.00 - 09.40
,,,,,TI22E,Rabu,10.30 - 12.10
,,Deep Learning,5,2,TI22A,Rabu,08.00 - 09.40
,,,,,TI22E,Kamis,08.00 - 09.40
6,"Ir. Kamdan, M.Kom",Organisasi dan arsitektur Komputer,1,2,TI24A,Rabu,13.00 - 14.40
,,,,,TI24G,Rabu,10.30 - 12.10
,,,,,TI24E,Senin,14.40 - 16.20
,,,,,TI24F,Senin,10.30 - 12.10
,,,,,TI24I,Rabu,14.40 - 16.20
,,,,,TI24T,Senin,13.00 - 14.40
,,Jaringan Komputer dan Keamanan Informasi,3,4,TI23B,Sabtu,14.30 - 16.30
7,"Dhita Diana Dewi, M.Stat",Statistika dan Probabilitas,1,3,TI24A,Senin,10.30 - 13.00
,,,,,TI24E,Senin,08.00 - 10.30
,,,,,TI24F,Selasa,08.00 - 10.30
,,,,,TI24G,Selasa,10.30 - 13.00
,,,,,TI24I,Kamis,13.00 - 15.30
,,,,,TI24T,kamis,16.00 - 18.30
8,"Lusiana Sani Parwati, M.Mat",Kalkulus,1,3,TI24I,Senin,16.00 - 18.30
,,,,,TI24T,Jumat,13.00 - 15.30
,,Metode Numerik,3,3,TI23H,Selasa,08.00 - 10.30
,,,,,TI23F,Selasa,16.00 - 18.30
,,,,,TI23I,Kamis,08.00 - 10.30
,,,,,TI23T,Selasa,10.30 - 13.00
9,"Drs. Nuzwan Sudariana, MM",Statistika dan Probabilitas,1,3,TI24M,Senin,18.30 - 20.00
,,,,,TI24C,Minggu,08.00 - 10.30
,,,,,TI24B,Sabtu,13.00- 14.30
,,Kalkulus,1,3,TI24E,Senin,10.30 - 13.00
,,,,,TI24F,Jumat,08.00 - 10.30
,,,,,TI24A,Senin,16.00 - 18.30
,,,,,TI24G,Senin,13.00 - 15.30
10,"Syahid Abdullah, S.Si.,M.Kom",Kalkulus,1,3,TI24H,Rabu,13.00 - 15.30 (online)
,,,,,TI24M,Kamis,18.30 - 20.00 (online)
,,Metode Numerik,3,3,TI23E,Rabu,10.30 - 13.00 (online)
,,,,,TI23M,Jumat,18.30 - 20.00 (online)
11,"Hermanto, M.Kom",Organisasi dan arsitektur Komputer,1,2,TI24M,Selasa,18.30 - 19.30
,,,,,TI24H,Rabu,10.30 - 12.10
,,Sistem Paralel dan Terdistribusi,3,2,TI23A,Rabu,13.00 - 14.40
,,,,,TI23E,Rabu,16.00-17.40
,,,,,TI23F,Selasa,10.30 - 12.10
,,,,,TI23G,Selasa,13.00-14.40
,,,,,TI23H,Kamis,13.00 - 15.30
,,,,,TI23J,Kamis,16.00 - 18.30
,,,,,TI23M,Selasa,19.30 - 20.30
,,,,,TI23B,Sabtu,online
,,,,,TI23C,Minggu,16.00 - 17.00
12,"Nugraha, M.Kom",Algoritma dan Struktur Data,1,4,TI24F,Senin,13.00 - 16.20
,,,,,TI24G,Senin,08.00 - 11.20
,,,,,TI24H,Jumat,08.00 - 11.20
,,Pemrograman Berbasis Platform,3,3,TI23J,Jumat,13.00 - 15.30
,,,,,TI23M,Senin,18.30 - 20.00
,,Pemrograman Berbasis Mobile,5,2,TI22F,Rabu,13.00 - 14.40
,,,,,TI22H,Rabu,10.30 - 12.10
,,,,,TI22M,Senin,20.00 - 21.00
13,"Imam Sanjaya, SP., M.Kom",Kalkulus,1,3,TI24B,Sabtu,19.00 - 20.30
,,,,,TI24C,Minggu,16.00 - 17.30
,,Metode Numerik,3,3,TI23B,Sabtu,17.00 - 18.30
,,,,,TI23C,Minggu,13.30 - 15.00
,,,,,TI23A,Kamis,13.00 - 15.30
,,,,,TI23G,Selasa,16.00 - 18.30
,,,,,TI23J,Selasa,13.00 - 15.30
,,Kompleksitas Algoritma,3,2,TI23E,Rabu,13.00 - 14.40
,,,,,TI23F,Rabu,16.00 -17.40
,,,,,TI23H,Kamis,16.00 - 17.40
,,,,,TI23M,Selasa,18.30 - 19.30
14,"Zaenal Alamsyah, M.Kom",Logika Informatika,1,3,TI24H,Kamis,13.00 - 15.30
,,Interaksi manusia dan Komputer,3,2,TI23B,Sabtu,online
,,,,,TI23C,Minggu,17.00 - 18.00
,,,,,TI23T,Rabu,13.00 - 14.40
,,Kompleksitas Algoritma,3,2,TI23A,Kamis,10.30 - 12.10
,,,,,TI23I,Rabu,10.30 - 12.10
,,Rekayasa Perangkat Lunak,3,3,TI23F,Kamis,16.00 - 18.30
,,,,,TI23H,Rabu,08.00 - 10.30
,,,,,TI23G,Selasa,08.00 - 10.30
,,Computer Vision,5,2,TI22C,Minggu,16.00 - 17.00
15,"M.Ikhsan Thohir, M.Kom",Algoritma dan Struktur Data,1,4,TI24I,Jumat,13.00 - 16.20
,,,,,TI24T,Selasa,13.00 - 16.20
,,Pemrograman Berbasis Platform,3,3,TI23A,Rabu,08.00 - 10.30
,,,,,TI23E,Senin,16.00 - 18.30
,,,,,TI23F,Kamis,10.30 - 13.00
,,Kompleksitas algoritma,3,2,TI23B,Sabtu,online
,,,,,TI23C,Minggu,online
,,,,,TI23T,Rabu,16.00 - 17.40
,,Sistem Informasi Geografis,5,2,TI22F,Selasa,08.00 - 09.40
,,,,,TI22H,Selasa,10.30 - 12.10
16,"Adrian Reza, M.Kom",Interaksi Manusia dan Komputer,3,2,TI23E,Selasa,16.00 - 17.40 (online)
,,,,,TI23M,Jumat,20.00 - 21.00 (online)
,,,,,TI23G,Rabu,16.00 - 17.40 (online)
,,,,,TI23J,Jumat,16.00 - 17.40 (online)
17,"Shinta Ayuningtyas, M.Kom",Algoritma dan Struktur Data,1,4,TI24E,Jumat,08.00 - 11.20
,,,,,TI24B,Sabtu,14.30 - 16.30
,,,,,TI24C,Minggu,13.00 - 15.00
,,Pemrograman Berbasis Platform,3,3,TI23B,Sabtu,13.00 - 14.30
,,,,,TI23C,Minggu,08.00 - 09.30
,,Basis Data,5,3,TI22B,Sabtu,13.00 - 14.30
,,,,,TI22C,Minggu,09.30 - 11.00
,,,,,TI22M,Jumat,18.30 - 20.00
18,"Moneyta Dholah Rosita, M.Kom",Rekayasa Perangkat Lunak,3,3,TI23A,Selasa,13.00 - 15.30
,,,,,TI23C,Minggu,09.30 - 11.00
,,Pengolahan Citra Digital,5,3,TI22F,Kamis,13.00 - 15.30
,,,,,TI22H,Selasa,16.00 - 18.30
,,,,,TI22M,Senin,18.30 - 20.00
19,"Mega Lumbia Octavia Sinaga, M.Kom",Rekayasa Perangkat Lunak,3,3,TI23I,Senin,16.00 - 18.00
,,,,,TI23T,Kamis,16.00 - 18.30
,,Pemrograman Berbasis Platform,3,3,TI23G,Rabu,13.00 - 15.30
,,Pengolahan Citra Digital,5,3,TI22I,Selasa,16.00 - 18.30
,,,,,TI22T,Rabu,16.00 - 18.30
20,"Indra Yustiana, M.Kom",Pengolahan Perangkat Lunak,5,3,TI22F,Selasa,16.00 - 18.30 (online)
,,,,,TI22B,Sabtu,online
,,,,,TI22C,Minggu,19.00 - 20.30 (online)
,,Etika Profesi,5,2,TI22C,Minggu,17.00 - 18.00 (online)
,,,,,TI22T,Jumat,16.00 - 17.400 (online)
,,,,,TI22M,Jumat,20.00 - 21.00 (online)
21,"Harris Al Qodri Maarif, S.T., M.Sc. P. hD",Projek Perangkat Lunak,5,3,TI22M,Selasa,20.00 - 21.30 (online)
,,,,,TI22H,Rabu,13.00 - 15.30 (online)
,,,,,TI22T,Kamis,13.00 - 15.30 (online)
,,Etika profesi,5,2,TI22I,Jumat,16.00 - 17.40 (online)
,,,,,TI22J,Rabu,16.00 - 17.40 (online)
22,"Dr. Iwan Setiawan, S.T., M.T",Metodelogi Penelitian,5,3,TI22H,Selasa,13.00 - 15.30 (online)
,,Etika Profesi,5,2,TI22E,Rabu,13.00 - 14.40 (online)
,,,,,TI22F,Jumat,13.00 - 14.40 (online)
,,Projek Perangkat Lunak,5,3,TI22J,Kamis,13.00 - 15.30 (online)
23,"Dede Sukmawan, M.Kom",Basis Data,5,3,TI22A,Rabu,13.00 - 15.30
,,,,,TI22F,Kamis,16.00 - 18.30
,,,,,TI22H,Kamis,13.00 - 15.30
24,"Falentino Sembiring, M.Kom",Basis Data,5,3,TI22E,Selasa,16.00 - 18.30
,,,,,TI22I,Kamis,16.00 - 18.30
,,Teknologi Blockchain,5,2,TI22B,Sabtu,14.30 - 15.30
,,,,,TI22J,Selasa,13.00 - 14.40
,,,,,TI22T,Selasa,16.00 - 17.40
25,Dr. Huang Gan,Data science,5,2,TI22I,Selasa,10.30 - 12.10
,,Deep Learning,5,2,TI22I,Selasa,13.00 - 14.40
,,Big Data Architecture and Infrastructure,5,2,TI22T,Jumat,13.00 - 14.40
26,"Muchtar Ali Setyo Yudono, S.T. M.T",Organisasi dan Arsitektur Komputer,1,2,TI24B,Sabtu,17.00 - 18.00
,,,,,TI24C,Minggu,10.30 - 11.30
,,Pengolahan Citra Digital,5,3,TI22B,Sabtu,18.30 - 20.00
,,,,,TI22C,Minggu,08.00 - 09.30
,,Deep Learning,5,2,TI22C,Minggu,13.00 - 14.00
27,Dr. Deni Hasman,Etika Profesi,5,2,TI22B,sabtu,online
,,,,,TI22A,Jumat,16.00 - 17.40
,,,,,TI22H,Jumat,14.00 - 15.40
28,Dr. Nurkhan,Metodelogi Penelitian,5,3,TI22E,Senin,16.00 - 18.30
29,Dr. Yurman Zaenal,Metodelogi Penelitian,5,3,TI22A,Selasa,16.00 - 18.30
30,"Zaenal Alamsyah, M.Kom// Dosen baru",Logika Informatika,1,3,TI24M,Jumat,18.30 - 20.00
,,,,,TI24C,Minggu,11.30-13.00
31,"Indra Yustiana, M.Kom// Dosen baru",Project Perangkat Lunak,5,3,TI22C,Minggu,17.00 - 18.00
32,Ir. Somantri//Dosen baru,Jaringan Komputer dan Keamanan Informasi,3,4,TI23A,Jumat,08.00 - 11.20
,,,,,TI23G,Kamis,13.00-16.20
,,,,,TI23H,Selasa,13.00 - 16.20
33,"Anggun Fergina, M.Kom// Dosen baru",Jaringan Komputer dan Keamanan Informasi,3,4,TI23J,Selasa,08.00 - 11.20
34,"Gina Purnama Insany, S.Si.T.,M.Kom//Dosen Baru",Logika Informatika,1,3,TI24B,Sabtu,online
35,"Moneyta Dholah Rosita, M.Kom// Dosen baru",Rekayasa Perangkat Lunak,3,3,TI23B,Sabtu,19.00 - 20.30
36,"Mega Lumbia Octavia Sinaga, M.Kom// Dosen baru",Rekayasa Perangkat Lunak,3,3,TI23E,Selasa,13.00 - 15.30
37,"Shinta Ayuningtyas, M.Kom// Dosen baru",Jaringan Komputer dan Keamanan Informasi,3,4,TI23M,Kamis,18.30 - 20.30
,,,,,TI23C,Minggu,16.00 -18.00
,,,,,,,
,Noted:,,,,,,
,,Menunggu dosen baru yang ditendem=12 kelas,,,,,
"""
}

# Yuk, kita muat data jadwal mata kuliahnya
mapping_mata_kuliah_df = pd.read_csv(
    StringIO(file_contents["Mapping Jadwal Mengajar Prodi Teknik Informatika.xlsx - Mapping mata kuliah.csv"]),
    skiprows=2 # Lewati 2 baris awal yang cuma judul
)

# --- PENTING BANGET: Langsung bersihin nama kolom setelah di-load ---
# Hapus spasi di awal/akhir nama kolom biar rapi
mapping_mata_kuliah_df.columns = mapping_mata_kuliah_df.columns.str.strip()

# --- 2. Beresin data mapping_mata_kuliah_df ---

# Isi nilai yang kosong buat 'Nama Dosen', 'Mata Kuliah', 'Semester', 'SKS', sama 'No'
# Soalnya kolom ini cuma diisi di baris pertama aja kalau dosennya sama
mapping_mata_kuliah_df['Nama Dosen'] = mapping_mata_kuliah_df['Nama Dosen'].ffill()
mapping_mata_kuliah_df['Mata Kuliah'] = mapping_mata_kuliah_df['Mata Kuliah'].ffill()
mapping_mata_kuliah_df['Semester'] = mapping_mata_kuliah_df['Semester'].ffill()
mapping_mata_kuliah_df['SKS'] = mapping_mata_kuliah_df['SKS'].ffill()
mapping_mata_kuliah_df['No'] = mapping_mata_kuliah_df['No'].ffill() # Pakai 'No' setelah spasi dihilangin

# Buang baris yang 'Kelas' atau 'Hari' atau 'Jam' nya masih kosong.
# Biasanya ini baris kosong atau catatan di akhir file yang bukan jadwal.
mapping_mata_kuliah_df.dropna(subset=['Kelas', 'Hari', 'Jam'], inplace=True)


# Ambil Waktu Mulai dan Selesai dari kolom 'Jam'
def parse_jam(jam_str):
    """
    Fungsi ini buat misahin waktu mulai dan selesai dari string 'Jam'.
    Bisa juga nanganin kalau ada tulisan 'online'.
    """
    if isinstance(jam_str, str):
        # Bersihin '(online)' kalau ada
        jam_str_cleaned = jam_str.replace('(online)', '').strip()
        if ' - ' in jam_str_cleaned:
            start_time, end_time = jam_str_cleaned.split(' - ')
            return start_time, end_time
        elif jam_str_cleaned.lower() == 'online':
            return 'Online', 'Online' # Buat kelas online yang nggak ada jam spesifiknya
    return None, None

mapping_mata_kuliah_df[['MULAI', 'SELESAI']] = mapping_mata_kuliah_df['Jam'].apply(
    lambda x: pd.Series(parse_jam(x))
)

# Ambil 'PRODI' (Program Studi) dan 'ANGKATAN' dari kolom 'Kelas'
# Format 'Kelas' itu kayak 'TI24A', 'TI23H', 'TI22M'
mapping_mata_kuliah_df['PRODI'] = 'Teknik Informatika' # Udah pasti ini sih, dari nama filenya
mapping_mata_kuliah_df['ANGKATAN'] = mapping_mata_kuliah_df['Kelas'].str.extract(r'TI(\d{2})[A-Z]').astype(float) # Ambil angka 2 digit tahun

# Ubah nama kolom 'Semester' jadi 'SMT' biar sama kayak format output yang diinginkan, terus jadiin angka
mapping_mata_kuliah_df['SMT'] = mapping_mata_kuliah_df['Semester'].astype(int)

# Tambahin kolom 'RUANG' kosong dulu, soalnya di data awal nggak ada
mapping_mata_kuliah_df['RUANG'] = 'TBD' # To Be Determined, atau bisa diisi ruangan spesifik nanti

# Pastiin SKS itu angka bulat
mapping_mata_kuliah_df['SKS'] = mapping_mata_kuliah_df['SKS'].astype(int)

# --- 3. Bikin DataFrame jadwal akhirnya ---
final_schedule_df = mapping_mata_kuliah_df[[
    'Hari', 'Mata Kuliah', 'Kelas', 'RUANG', 'MULAI', 'SELESAI', 'SKS', 'SMT', 'PRODI'
]].copy()

# Ganti nama kolom biar sama persis kayak di contoh output gambar
final_schedule_df.rename(columns={
    'Hari': 'HARI',
    'Mata Kuliah': 'MATAKULIAH',
    'Kelas': 'KELAS',
    'MULAI': 'MULAI',
    'SELESAI': 'SELESAI',
    'SKS': 'SKS',
    'SMT': 'SMT',
    'PRODI': 'PRODI'
}, inplace=True)

# Urutin hari biar jadwalnya runtut dari Senin sampai Minggu
day_order = ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu']
final_schedule_df['HARI'] = pd.Categorical(final_schedule_df['HARI'], categories=day_order, ordered=True)

# Urutin jadwalnya berdasarkan Hari, terus Waktu Mulai, baru Kelasnya
final_schedule_df.sort_values(by=['HARI', 'MULAI', 'KELAS'], inplace=True)
final_schedule_df.reset_index(drop=True, inplace=True)


# --- 4. Fungsi-fungsi buat Ngurus Jadwal ---

def check_schedule_conflict(df, new_hari, new_kelas, new_mulai, new_selesai, exclude_index=None):
    """
    Ngecek ada bentrok jadwal nggak sih buat kelas dan waktu yang kita masukin.
    Bentrok itu kalau ada jadwal yang sama buat kelas itu, di hari yang sama,
    dan jamnya tumpang tindih.
    exclude_index ini buat ngabaikan baris tertentu (misal, baris yang lagi diedit).
    """
    
    # Buat kelas 'Online', ini beda ya. Dia nggak bentrok sama kelas fisik atau online lain
    # kecuali kalau kelasnya bener-bener sama persis. Anggap aja gitu biar gampang.
    if new_mulai.lower() == 'online' and new_selesai.lower() == 'online':
        # Kalau jadwal baru ini online, cek ada nggak jadwal online yang sama persis
        conflict = df[
            (df['HARI'] == new_hari) &
            (df['KELAS'] == new_kelas) &
            (df['MULAI'].str.lower() == 'online') &
            (df['SELESAI'].str.lower() == 'online')
        ]
        if exclude_index is not None:
            conflict = conflict[conflict.index != exclude_index]
        return not conflict.empty # True kalau ada bentrok, False kalau aman

    # Ubah format waktu biar bisa dibandingin (misal, jadi total menit dari tengah malam)
    # Untuk format HH.MM, bandingin langsung pakai string juga bisa sih, asalkan urut.
    # Tapi ini kita pakai logika tumpang tindih waktu yang bener.
    
    # Filter dulu buat hari dan kelas yang sama
    potential_conflicts = df[
        (df['HARI'] == new_hari) &
        (df['KELAS'] == new_kelas) &
        (df['MULAI'].str.lower() != 'online') # Nggak usah cek kelas online buat bentrok waktu fisik
    ]

    if exclude_index is not None:
        potential_conflicts = potential_conflicts[potential_conflicts.index != exclude_index]

    for index, existing_row in potential_conflicts.iterrows():
        existing_mulai = existing_row['MULAI']
        existing_selesai = existing_row['SELESAI']

        # Cek kalau ada tumpang tindih: (mulai_baru < selesai_lama) dan (mulai_lama < selesai_baru)
        # Asumsi format HH.MM bisa langsung dibandingin stringnya
        if (new_mulai < existing_selesai) and (existing_mulai < new_selesai):
            return True # Wah, bentrok nih!

    return False # Aman, nggak ada bentrok

def display_schedule(df):
    """Nampilin jadwal yang udah ada."""
    if df.empty:
        print("\nJadwalnya masih kosong nih.")
    else:
        print("\n--- Jadwal Kuliah Kita Sekarang ---")
        # Pake to_string() dari pandas biar tabelnya rapi
        print(df.to_string(index=True)) # Tunjukin indeksnya biar gampang kalau mau ubah

def add_schedule_entry(df):
    """Nambahin jadwal baru ke daftar jadwal."""
    print("\n--- Yuk, Tambah Jadwal Baru! ---")
    try:
        hari = input("Hari (Senin, Selasa, dll.): ").strip().capitalize()
        if hari not in day_order:
            print("Harinya nggak valid nih. Coba masukin hari yang bener ya.")
            return df
        matakuliah = input("Nama Mata Kuliah: ").strip()
        kelas = input("Kelas (contoh: TI24A): ").strip().upper()
        ruang = input("Ruang (contoh: Lab 101, TBD): ").strip()
        mulai = input("Waktu Mulai (HH.MM, atau 'online'): ").strip()
        selesai = input("Waktu Selesai (HH.MM, atau 'online'): ").strip()
        
        # Cek format waktu kalau bukan 'online'
        if mulai.lower() != 'online' and not pd.Series([mulai]).str.match(r'^\d{2}\.\d{2}$').all():
            print("Format waktu mulainya salah. Pake HH.MM ya.")
            return df
        if selesai.lower() != 'online' and not pd.Series([selesai]).str.match(r'^\d{2}\.\d{2}$').all():
            print("Format waktu selesainya salah. Pake HH.MM ya.")
            return df

        # --- Cek Bentrok ---
        if check_schedule_conflict(df, hari, kelas, mulai, selesai):
            print(f"Duh, jadwal buat Kelas '{kelas}' di hari '{hari}' jam {mulai}-{selesai} udah ada atau bentrok nih.")
            return df # Balikin DataFrame awal aja kalau bentrok

        sks = int(input("SKS-nya berapa: "))
        smt = int(input("Semester berapa: "))
        prodi = input("Program Studi (contoh: Teknik Informatika): ").strip()

        new_entry = pd.DataFrame([{
            'HARI': hari,
            'MATAKULIAH': matakuliah,
            'KELAS': kelas,
            'RUANG': ruang,
            'MULAI': mulai,
            'SELESAI': selesai,
            'SKS': sks,
            'SMT': smt,
            'PRODI': prodi
        }])

        df = pd.concat([df, new_entry], ignore_index=True)
        # Urutkan lagi setelah ditambah biar tetap rapi
        df['HARI'] = pd.Categorical(df['HARI'], categories=day_order, ordered=True)
        df.sort_values(by=['HARI', 'MULAI', 'KELAS'], inplace=True)
        df.reset_index(drop=True, inplace=True)
        print("Jadwalnya berhasil ditambahkan!")
    except ValueError:
        print("Inputnya nggak bener nih. Pastiin SKS dan Semester itu angka ya, dan jamnya format HH.MM.")
    except Exception as e:
        print(f"Ada masalah waktu nambahin jadwal: {e}")
    return df

def delete_schedule_entry(df):
    """Ngilangin jadwal dari daftar berdasarkan nomor indeks yang muncul."""
    print("\n--- Hapus Jadwal Yuk ---")
    if df.empty:
        print("Jadwalnya kosong nih, nggak ada yang bisa dihapus.")
        return df

    display_schedule(df) # Tunjukin jadwal lengkap dengan indeksnya biar gampang
    try:
        index_to_delete = int(input("Masukkan nomor indeks jadwal yang mau dihapus: "))
        if index_to_delete in df.index:
            df = df.drop(index_to_delete).reset_index(drop=True)
            print(f"Jadwal dengan indeks {index_to_delete} berhasil dihapus.")
        else:
            print("Indeksnya nggak valid nih. Coba masukin indeks yang ada di jadwal ya.")
    except ValueError:
        print("Inputnya salah. Masukin angka aja buat indeksnya.")
    except Exception as e:
        print(f"Ada masalah waktu ngehapus jadwal: {e}")
    return df

def modify_schedule_entry(df):
    """Ngubah jadwal yang udah ada berdasarkan indeksnya."""
    print("\n--- Yuk, Ubah Jadwal ---")
    if df.empty:
        print("Jadwalnya kosong nih, nggak ada yang bisa diubah.")
        return df

    display_schedule(df) # Tunjukin jadwal lengkap dengan indeksnya
    try:
        index_to_modify = int(input("Masukkan nomor indeks jadwal yang mau diubah: "))
        if index_to_modify not in df.index:
            print("Indeksnya nggak valid nih. Coba masukin indeks yang ada di jadwal ya.")
            return df

        print(f"\nKita ubah jadwal di indeks {index_to_modify} ya:")
        current_entry = df.loc[index_to_modify].copy() # Ambil data barisnya buat diubah

        print(f"Data sekarang: Hari={current_entry['HARI']}, Matakuliah={current_entry['MATAKULIAH']}, Kelas={current_entry['KELAS']}")
        
        hari = input(f"Hari baru ({current_entry['HARI']}): ").strip().capitalize() or current_entry['HARI']
        if hari not in day_order:
            print("Harinya nggak valid. Coba masukin hari yang bener ya.")
            return df

        matakuliah = input(f"Nama Mata Kuliah baru ({current_entry['MATAKULIAH']}): ").strip() or current_entry['MATAKULIAH']
        kelas = input(f"Kelas baru ({current_entry['KELAS']}): ").strip().upper() or current_entry['KELAS']
        ruang = input(f"Ruang baru ({current_entry['RUANG']}): ").strip() or current_entry['RUANG']
        mulai = input(f"Waktu Mulai baru ({current_entry['MULAI']}): ").strip() or current_entry['MULAI']
        selesai = input(f"Waktu Selesai baru ({current_entry['SELESAI']}): ").strip() or current_entry['SELESAI']

        # Cek format waktu kalau bukan 'online'
        if mulai.lower() != 'online' and not pd.Series([mulai]).str.match(r'^\d{2}\.\d{2}$').all():
            print("Format waktu mulainya salah. Pake HH.MM ya.")
            return df
        if selesai.lower() != 'online' and not pd.Series([selesai]).str.match(r'^\d{2}\.\d{2}$').all():
            print("Format waktu selesainya salah. Pake HH.MM ya.")
            return df

        # --- Cek Bentrok buat perubahan ---
        # Masukin indeksnya biar dia nggak dicek bentrok sama dirinya sendiri
        if check_schedule_conflict(df, hari, kelas, mulai, selesai, exclude_index=index_to_modify):
            print(f"Duh, jadwal buat Kelas '{kelas}' di hari '{hari}' jam {mulai}-{selesai} bentrok sama jadwal lain nih.")
            return df

        sks_input = input(f"SKS baru ({current_entry['SKS']}): ").strip()
        sks = int(sks_input) if sks_input else current_entry['SKS']

        smt_input = input(f"Semester baru ({current_entry['SMT']}): ").strip()
        smt = int(smt_input) if smt_input else current_entry['SMT']
        
        prodi = input(f"Program Studi baru ({current_entry['PRODI']}): ").strip() or current_entry['PRODI']

        # Update data di baris DataFrame
        df.loc[index_to_modify] = {
            'HARI': hari,
            'MATAKULIAH': matakuliah,
            'KELAS': kelas,
            'RUANG': ruang,
            'MULAI': mulai,
            'SELESAI': selesai,
            'SKS': sks,
            'SMT': smt,
            'PRODI': prodi
        }
        
        # Urutkan lagi setelah diubah biar tetap rapi
        df['HARI'] = pd.Categorical(df['HARI'], categories=day_order, ordered=True)
        df.sort_values(by=['HARI', 'MULAI', 'KELAS'], inplace=True)
        df.reset_index(drop=True, inplace=True)
        print("Jadwalnya berhasil diubah!")

    except ValueError:
        print("Inputnya nggak bener nih. Pastiin SKS dan Semester itu angka ya, dan jamnya format HH.MM.")
    except Exception as e:
        print(f"Ada masalah waktu ngubah jadwal: {e}")
    return df


def export_schedule_to_excel(df):
    """Nge-ekspor jadwal yang sekarang ke file Excel."""
    print("\n--- Yuk, Eksport Jadwal ke Excel ---")
    if df.empty:
        print("Jadwalnya kosong nih, nggak ada yang bisa diekspor.")
        return

    file_name = input("Mau simpan jadi file Excel apa namanya? (contoh: jadwal_kuliah.xlsx): ").strip()
    if not file_name.lower().endswith('.xlsx'):
        file_name += '.xlsx' # Tambahin .xlsx kalau belum ada
    
    try:
        df.to_excel(file_name, index=False)
        print(f"Jadwalnya berhasil diekspor ke '{file_name}'!")
    except Exception as e:
        print(f"Ada masalah waktu ngekspor jadwal ke Excel: {e}")


# --- 5. Program Utama Kita ---
if __name__ == "__main__":
    current_schedule_df = final_schedule_df.copy() # Pake kopiannya aja biar yang asli aman kalau diutak-atik

    while True:
        print("\n" + "="*50)
        print("          Sistem Manajemen Jadwal         ")
        print("          Universitas Nusaputra           ")
        print("="*50)
        print("1. Lihat Jadwal Sekarang")
        print("2. Tambah Jadwal Baru")
        print("3. Hapus Jadwal")
        print("4. Ubah Jadwal")
        print("5. Eksport Jadwal ke Excel")
        print("6. Keluar Aplikasi")
        print("="*50)

        choice = input("Pilih maunya yang mana nih (1-6): ")

        if choice == '1':
            display_schedule(current_schedule_df)
        elif choice == '2':
            current_schedule_df = add_schedule_entry(current_schedule_df)
        elif choice == '3':
            current_schedule_df = delete_schedule_entry(current_schedule_df)
        elif choice == '4':
            current_schedule_df = modify_schedule_entry(current_schedule_df)
        elif choice == '5':
            export_schedule_to_excel(current_schedule_df)
        elif choice == '6':
            print("\nMakasih ya udah pake aplikasi ini. Sampai jumpa!")
            print("="*50)
            break
        else:
            print("\nPilihannya nggak ada nih. Coba masukin angka 1 sampai 6 ya.")
            print("="*50)