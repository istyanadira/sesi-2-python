a = int(input("Masukkan nilai x: "))
b = int(input("Masukkan nilai y: "))
x = a % 2
y = b % 2

bx = (bool(x))
by = (bool(y))

def pilih():
    print('1. AND')
    print('2. OR')
    print('3. NOT')
    print('4. XOR')
    print('5. Keluar')

pilih()
opsi = int(input('Pilih menu yang akan dipakai: '))

while opsi != 5:
    if opsi == 1:
        dan = bx and by
        print('Karena x adalah', bx, 'dan y adalah', by, 'jadi hasilnya adalah', dan)
    elif opsi == 2:
        atau = bx or by
        print('Karena x adalah', bx, 'dan y adalah', by, 'jadi hasilnya adalah', atau)
    elif opsi == 3:
        tx = not bx
        ty = not by
        print('1. NOT X')
        print('2. NOT Y')
        opsi1 = int(input('Pilih disini: '))
        if opsi1 == 1:
            print("Karna x adalah", bx, 'jadi NOT x adalah', tx)
        elif opsi1 == 2:
            print("Karna y adalah", by, 'jadi NOT y adalah', ty)
    elif opsi == 4:
        sor = bx ^ by
        print(print('Karena x adalah', bx, 'dan y adalah', by, 'jadi hasilnya adalah', sor))
    pilih()
    opsi = int(input('Pilih menu yang akan dipakai: '))

print('Terima kasih')