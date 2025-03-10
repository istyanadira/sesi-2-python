usia = int(input("Masukkan usia anak Anda: "))

if int(usia) <= 2:
    print("Anak anda masuk kategori Bayi")
elif 2 <= usia <= 5:
    print("Anak anda masuk kategori Balita")
elif 5 <= usia <= 12:
    print("Anak anda masuk kategori Anak-anak")
elif 12 <= usia <= 18:
    print("Anak anda masuk kategori Remaja")

else:
    print("Anak anda masuk kategori Dewasa")