angka1 = int(input("Angka pertama: "))
angka2 = int(input("Angka kedua: "))
aritmatik = input("Pilih operator aritmatika (+,-,*,/): ")
if aritmatik == "+":
    hasil_tambah = angka1 + angka2
    print("Hasil pertambahannya adalah %s" % (hasil_tambah))
elif aritmatik == "-":
    hasil_kurang = angka1 - angka2
    print("Hasil pengurangannya adalah %s" % (hasil_kurang))
elif aritmatik == "*":
    hasil_kali = angka1 * angka2
    print("Hasil perkaliannya adalah %s" % (hasil_kali))
elif aritmatik == "/" and angka2 > 0:
    hasil_bagi = angka1 / angka2
    print("Hasil pembagiannya adalah %s" % (hasil_bagi))
else:
    print("Program error")