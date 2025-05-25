from datetime import datetime

def hitung_umur(tahun_lahir):
    tahun_ini = datetime.now().year
    umur = tahun_ini - tahun_lahir
    return umur

tahun_lahir = int(input("Masukkan tahun lahir Anda: "))
umur = hitung_umur(tahun_lahir)
print("Umur", umur , "Tahun")