#biaya = input("Apakah Anda sudah membayar UKT? (S/B): ")
#syarat_lulus = 0;
#if biaya == "s" or "S":
    #syarat_lulus += 1
#ujian = input ("Kategori apa nilai rata-rata Anda? (A/B/C/D/E): ")
#if ujian == "A" or "B" or "C":
    #syarat_lulus += 1
#if syarat_lulus == 2:
    #print("Syarat untuk lulus terpenuhi")
    #print("Anda Lulus")
#else:
    #print("Syarat untuk lulus tidak terpenuhi")
    #print("Anda Tidak Lulus")

is_bayar = input("Apakah sudah membayar UKT? (Sudah / Belum): ")
nilai_d = input("Apakah Anda memiliki nilai D? (Ya / Tidak): ")

if (is_bayar == "Sudah" and nilai_d == "Tidak"):
    print("Selamat Anda Lulus!")
else:
    print("Anda Tidak Lulus")




