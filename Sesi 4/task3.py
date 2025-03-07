total = int(input("Masukkan total belanja: Rp. "))
if total >= 100000:
    dis10 = total * 0.1
    hasil10 = total - dis10
    print("Total belanjaan: Rp. ", total)
    print("Mendapatkan diskon 10% menjadi: Rp. ", hasil10)
elif total >= 50000:
    dis5 = total * 0.05
    hasil5 = total - dis5
    print("Total belanjaan: Rp. ", total)
    print("Mendapatkan diskon 5% menjadi: Rp. ", hasil5)
else:
    print("Total belanjaan: Rp: ", total)