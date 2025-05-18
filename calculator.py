a = int(input("Masukkan angka pertama: "))
b = int(input("Masukkan angka kedua: "))

def pilih():
    print("1. Pertambahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    print("5. Keluar")

pilih()
opsi = int(input("Pilih operator aritmatika: "))

while opsi != 5:
    if opsi == 1:
        tambah = a + b
        print("Hasil penjumlahannya adalah ", tambah)
    elif opsi == 2:
        kurang = a - b
        print("Hasil pengurangannya adalah ", kurang)
    elif opsi == 3:
        kali = a * b
        print("Hasil perkaliannya adalah ", kali)
    elif opsi == 4:
        bagi = a / b
        print("Hasil pemabagiannya adalah ", bagi)
    pilih()
    opsi = int(input("Pilih operator aritmatika: "))
    
print("Hanupis")