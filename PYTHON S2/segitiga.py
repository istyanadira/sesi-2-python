tinggi = int(input('Masukan nilai a (tinggi): '))
alas = int(input('Masukan nilai b (alas): '))
c = int(input('Masukan nilai c: '))

def rumus():
    print('1. keliling')
    print('2. luas')
    print('3. keluar')

rumus()
pilihan = int(input('Masukan rumus yang dituju: '))

while pilihan != 3:
    if pilihan == 1:
        keliling = tinggi + alas + c
        print('Dengan rumus a+b+c. Keliling segitiga siku-siku ini adalah', keliling)
        rumus()
        pilihan = int(input('Masukan rumus yang dituju: '))

    elif pilihan == 2:
        luas = 0.5 * alas * tinggi
        print('Dengan rumus  ½ x a x t Luas dari Segitiga siku-siku ini adalah', luas)
        rumus()
        pilihan = int(input('Masukan rumus yang dituju: '))

print('Terima kasih! :)')