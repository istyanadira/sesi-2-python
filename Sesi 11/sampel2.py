def selamat_datang(nama):
    print(f"Halo {nama}, selamat datang!")

selamat_datang("Nurul")
selamat_datang("Lendis")
selamat_datang("Fabri")
selamat_datang("Isa")

def welcome(name):
    print("Halo", name, "selamat datang!")

def welcFromArr(names):
    for name in names:
        print("Halo", name, "selamat datang!")

names = ["Nurul", "Lendis", "Fabri", "Isa"]
for name in names:
    welcome(name)
    
welcFromArr(names)