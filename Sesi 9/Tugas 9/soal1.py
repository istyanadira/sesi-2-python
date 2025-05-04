box = []
for i in range(10):
    isi_box = int(input("Masukkan angka ke-%s: "%(i+1)))
    box.append(isi_box)
print()
print("Isi dari list angka yang nada masukkan adalah: ")
print(box)
print("Maka total dari semua angka di atas adalah %s"%(sum(box)))