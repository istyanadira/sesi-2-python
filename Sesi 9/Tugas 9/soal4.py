from statistics import median

isi_angka = input("Masukkan beberapa angka unutk di isi ke dalam list dan pisahkan dengan spasi (min 5 angka): ")
angka = list(map(int, isi_angka.split(' ')))
susun_angka = sorted(angka)
print()
print("Dengan data yang di input, kita bisa membuat list seperti ini: ")
print(angka)
print("Ini adalah list yang tersusun dari terkecil hingga terbesar: ")
print(susun_angka)
print("Terbesar: %s"%(max(susun_angka)))
print("Terkecil: %s"%(min(susun_angka)))
print("Median: %s"%(median(susun_angka)))