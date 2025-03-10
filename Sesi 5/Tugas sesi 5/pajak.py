harga = int(input("Masukkan harga kendaraan: "))
mobil = 143000
motor = 35000
njkb = 2;
plus_njkb = 5 
nilai_jual = int(input("Masukkan NJPB Anda: "))
if nilai_jual == 1:
    njkb += 0
elif nilai_jual > 1:
    njkbawal = nilai_jual - 1
    pnjkb = njkbawal * plus_njkb
    pajak = (pnjkb/10) + njkb
    njkb += pajak - 2
kendaraan = input("Masukkan jenis kendaraan: ")
if kendaraan == "Motor" or "motor":
    pajak_motor = (harga * (njkb/100)) + motor
    print("Pajak kendaraan Anda adalah %s" % (pajak_motor))
elif kendaraan == "Mobil" or "mobil":
    pajak_mobil = (harga * (njkb/100)) + mobil
    print("Pajak kendaraan Anda adalah %s" % (pajak_mobil))