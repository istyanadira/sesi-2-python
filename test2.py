s = (input('Masukan inputan data ke 1: '))
i = (input('Masukan inputan data ke 2: '))
f = (input("Masukan Inputan Data ke 3: "))

fs = str(s)
fi = int(i)
ff = float(f)
if type(string) is str:
    js += 1
if type(integer) is int:
    ji += 1
if type(flot) is float:
    jf += 1
if js == 0:
    print('Tipe data String tidak valid')
    if ji == 0:
        print('Tipe data Integer tidak valid')
        if jf == 0:
            print('Tipe data Float tidak valid')
else:
    print('Semua tipe data Valid')