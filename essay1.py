mesin = input("Masukkan harga mesin: ")
manfaat = input("Masukkan masa manfaat: ")
sisa = input("Masukkan nilai sisa: ")

susut_tahunan = int(mesin) - int(sisa)
susut_tahunan2 = int(susut_tahunan) / int(manfaat)
penyusutan = int(susut_tahunan2) * 2
nilai_aset = int(mesin) - int(penyusutan)
print("Jadi Nilai Aset tersisa: ", nilai_aset)
