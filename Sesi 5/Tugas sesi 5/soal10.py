import random

def pilihan_komputer():
    return random.choice(['batu', 'gunting', 'kertas'])

def tentukan_pemenang(pemain, komputer):
    if pemain == komputer:
        return 'seri'
    elif (pemain == 'batu' and komputer == 'gunting') or (pemain == 'gunting' and komputer == 'kertas') or (pemain == 'kertas' and komputer == 'batu'):
        return 'pemain'
    else:
        return 'komputer'
    
def main():
        skor_pemain = 0
        skor_komputer = 0

        print("Selamat datang di permainan Batu Gunting Kertas!")

        while True:
            print("Pilihan: batu, gunting, kertas")
            pemain = input("Masukkan pilihan Anda: ").lower()

            if pemain not in ['batu', 'gunting', 'kertas']:
                 print("Input tidak valid. Silahkan pilih anatar batu, gunting, kertas.")
                 continue
            
            komputer = pilihan_komputer()
            print(f"Komputer memilih: {komputer}")

            hasil = tentukan_pemenang(pemain, komputer)

            if hasil == 'seri':
                 print("Hasil seri")
            elif hasil == 'pemain':
                 print("Anda menang")
                 skor_pemain += 1
            else:
                 print("Komputer menang")
                 skor_komputer += 1

            print(f"Skor - Anda: {skor_pemain} | Komputer: {skor_komputer}")

            lanjut = input("Ingin bermain lagi? (Ya/Tidak): ").lower()
            if lanjut != 'Ya' or 'ya':
                 print("Terima kasih sudah bermain!")
                 break
            
if __name__ == '__main__':
     main()
            