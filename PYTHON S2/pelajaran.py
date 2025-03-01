nilai = 0;

IPA = int(input("Masukkan nilai IPA: "))
nilai += IPA
IPS = int(input("Masukkan nilai IPS: "))
nilai += IPS
MTK = int(input("Masukkan nilai MTK: "))
nilai += MTK
English = int(input("Masukkan nilai English: "))
nilai += English
Indonesia = int(input("Masukkan nilai Indonesia: "))
nilai += Indonesia

rata = nilai / 5
print("Jadi nilai rata-rata seorang siswa adalah", rata)

number = rata

if number > 75:
    print("Lulus")
if nilai <= 50:
    print("Lulus")
if nilai == 100:
    print("Lulus")

else :
    print("Tidak Lulus")




















































