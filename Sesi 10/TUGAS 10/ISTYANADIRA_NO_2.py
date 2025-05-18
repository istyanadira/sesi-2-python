mahasiswa = {}

def tambah_mahasiswa():
    nim = input("Masukkan NIM: ")
    if nim in mahasiswa:
        print("NIM sudah terdaftar")
        return
    nama = input("Masukkan Nama: ")
    jurusan = input("Masukkan Jurusan: ")
    try:
        ipk = float(input("Masukkan nilai IPK: "))
    except ValueError:
        print("IPK harus berupa angka")
        return
    mahasiswa[nim] = {"Nama": nama, "Jurusan": jurusan, "IPK": ipk}
    print("Data mahasiswa telah berhasil ditambahkan")

def tampilkan_semua():
    if not mahasiswa:
        print("Data mahasiswa masih kosong")
        return
    print("Data mahasiswa: ")
    for nim, data in mahasiswa.items():
        print(f"NIM: {nim}, Nama: {data["Nama"]}, Jurusan: {data["Jurusan"]}, IPK: {data["IPK"]}")

def cari_mahasiswa():
    nim = input("Masukkan NIM yang akan dicari: " )
    data = mahasiswa.get(nim)
    if data:
        print(f"NIM: {nim}, Nama: {data["Nama"]}, Jurusan: {data["Jurusan"]}, IPK: {data["IPK"]}")
    else:
        print("Data mahasiswa yang dicari tidak ditemukan")

def hapus_mahasiswa():
    nim = input("Masukkan NIM yang akan di hapus: ")
    if nim in mahasiswa:
        del mahasiswa[nim]
        print("Data mahasiswa berhasil di hapus")
    else:
        print("Data mahasiswa tidak ditemukan")

def menu():
    while True:
        print("\nMenu: ")
        print("1. Tambahkan data mahasiswa")
        print("2. Tampilkan semua data mahasiswa")
        print("3. Cari data mahasiswa berdasarkan NIM")
        print("4. Menghapus data mahasiswa berdasarkan NIM")
        print("5. Keluar")
        pilihan = input("Pilih menu: ")
        if pilihan == "1":
            tambah_mahasiswa()
        elif pilihan == "2":
            tampilkan_semua()
        elif pilihan == "3":
            cari_mahasiswa()
        elif pilihan == "4":
            hapus_mahasiswa()
        elif pilihan == "5":
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid")

if __name__ == "__main__":
    menu()