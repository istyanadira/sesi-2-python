nama = input("Masukkan nama: ")
box = "*"

for i in range(len(nama)):
    for a in range(1):
        nama += box
        box += "*"
        print(nama)