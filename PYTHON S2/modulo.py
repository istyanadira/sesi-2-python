uang = int(input("Masukkan jumlah uang: "))

ratusan = uang / 100000
limapuluhribu = uang / 50000
duapuluhribu = uang / 20000
puluhribu = uang / 10000
limaribu = uang / 5000
duaribu = uang / 2000
seribu = uang / 1000
perak = uang / 500

print("Jumlah ratusan: ", int(ratusan))
print("Jumlah 50 ribuan: ", int(limapuluhribu))
print("Jumlah 20 ribuan: ", int(duapuluhribu))
print("Jumlah 10 ribuan: ", int(puluhribu))
print("Jumlah 5 ribuan: ", int(limaribu))
print("Jumlah 2 ribuan: ", int(duaribu))
print("Jumlah 1 ribuan: ", int(seribu))
print("Jumlah 500 perak: ", int(perak))