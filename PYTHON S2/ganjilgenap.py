a = int(input("Masukan angkanya A: "))
b = int(input("Masukan angkanya B: "))
c = int(input("Masukan angkanya C: "))

ganjil = (c % 2) != 0
genap = (a % 2) == 0
if a > b and b > c and b != c and ganjil is True and genap is True:
    print('Kode Valid')

if ganjil is False:
    print('Kode salah karna c bukan ganjil')
if genap is False:
    print('Kode salah karna a bukan genap')
if a < b:
    print('Kode salah karna a lebih kecil daripada b')
if b < c:
    print('Kode salah karna b lebih kecil daripada c')
if b == c:
    print('Kode salah karna b dan c nilainya sama')