iventaris = {}

def tambah_barang():
    nama = input("Masukkan nama barang: ")
    if nama in iventaris:
        print("Barang sudah ada dalam iventaris")
        return
    try:
        harga = float(input("Masukkan harga barang: "))
        stok = int(input("Masukkan stok barang: "))
    except ValueError:
        print("Harga dan stok harus berupa angka")
        return
    iventaris[nama] = (harga, stok)
    print("Barang berhasil ditambahkan")

def tampilkan_barang():
    if not iventaris:
        print("Tidak ada barang dalam iventaris")
        return
    print("{:<20} {:<10} {:<10}".format ("Nama Barang", "Harga", "Stok"))
    print("-" * 40)
    for nama, (harga, stok) in iventaris.items():
        print("{:<20} {:<10} {:<10}".format(nama, harga, stok))

def cari_barang():
    nama = input("Masukkan nama barang yang dicari: ")
    if nama in iventaris:
        harga, stok = iventaris[nama]
        print(f"Nama: {nama}, Harga: {harga}, Stok: {stok}")
    else:
        print("Barang tidak ditemukan dalam iventaris")

def perbarui_barang():
    nama = input("Masukkan nama barang yang ingin diperbarui: ")
    if nama in iventaris:
        try:
            stok_baru = int(input("Masukkan stok baru: "))
        except ValueError:
            print("Stok harus berupa angka")
            return
        harga, _ = iventaris[nama]
        iventaris[nama] = (harga, stok_baru)
        print("Stok barang berhasil diperbarui")
    else:
        print("Barang tidak ditemukan dalam iventaris")

def hapus_barang():
    nama = input("Masukkan nama barang yang ingin dihapus: ")
    if nama in iventaris:
        del iventaris[nama]
        print("Barang berhasil dihapus")
    else:
        print("Barang tidak ditemukan dalam iventaris")

def analisis_barang():
    if not iventaris:
        print("Tidak ada barang dalam iventaris")
        return
    harga_tertinggi = max(iventaris.items(), key=lambda x: x[1][0])
    harga_terendah = min(iventaris.items(), key=lambda x: x[1][0])
    total_stok = sum(harga * stok for harga, stok in iventaris.values())
    print(f"Barang dengan harga tertinggi: {harga_tertinggi[0]} (Rp{harga_tertinggi[1][0]})")
    print(f"Barang dengan harga terendah: {harga_terendah[0]} (Rp{harga_terendah[1][0]})")
    print(f"Total nilai iventaris: Rp{total_stok}")

def menu():
    while True:
        print("\nMenu:")
        print("1. Tambah barang")
        print("2. Tampilkan barang")
        print("3. Cari barang")
        print("4. Perbarui barang")
        print("5. Hapus barang")
        print("6. Analisis barang")
        print("7. Keluar")
        pilihan = input("Pilih menu: ")
        
        if pilihan == '1':
            tambah_barang()
        elif pilihan == '2':
            tampilkan_barang()
        elif pilihan == '3':
            cari_barang()
        elif pilihan == '4':
            perbarui_barang()
        elif pilihan == '5':
            hapus_barang()
        elif pilihan == '6':
            analisis_barang()
        elif pilihan == '7':
            print("Terima kasih")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi")

if __name__ == "__main__":
    menu()
