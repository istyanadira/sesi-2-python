harga = input("Masukkan harga barang: ")
diskon = 0.20
harga_asli = int(harga) * diskon
harga_akhir = int(harga) - int(harga_asli)
print("Harga setelah diskon adalah Rp.", harga_akhir)