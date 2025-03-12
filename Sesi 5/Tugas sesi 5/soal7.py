berat = float(input("Masukkan berat badan (dalam satuan KG): "))
tinggi = float(input("Masukkan tinggi badan (dalam satuan M): "))
tinggi2 = tinggi ** 2
hasil = berat / tinggi2

if hasil >= 30.0:
    kategori = "obesitas"
elif hasil >= 25.0 and hasil < 30.0:
    kagetori = "kelebihan berat badan"
elif hasil >= 18.5 and hasil < 25.0:
    kategori = "normal"
else:
    kategori = "kekurangan berat badan"

print("Dengan BMI %s, maka kamu termasuk ke dalam kategori %s" % (hasil, kategori))