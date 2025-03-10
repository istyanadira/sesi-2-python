tahun = int(input("Masukkan tahun: "))
keterangan = "tahun kabisat" if tahun % 4 == 0 and tahun % 100 != 0 or tahun % 400 == 0 else "bukan tahun kabisat"
print("Tahun %s adalah %s" % (tahun, keterangan))