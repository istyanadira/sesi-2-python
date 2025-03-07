mtk = int(input("Masukkan nilai Matematika: "))
sains = int(input("Masukkan nilai Sains: "))
inggris = int(input("Masukkan nilai Bahasa Inggris: "))

rata_rata = (mtk + sains + inggris) / 3
bawah_70 = 0;
nilai_sempurna = 0;

if mtk == 100:
    nilai_sempurna += 1
if sains == 100:
    nilai_sempurna += 1
if inggris == 100:
    nilai_sempurna += 1
if mtk < 70:
    bawah_70 += 1
if sains < 70:
    bawah_70 += 1
if inggris < 70:
    bawah_70 += 1

if rata_rata >= 75:
    print("Kamu lulus dengan nilai rata rata %s" % (rata_rata))
elif nilai_sempurna >= 1:
    print("Kamu lulus dengan %s nilai sempurna" % (nilai_sempurna))
elif bawah_70 < 1:
    print("Kamu lulus dengan %s nilai dibawah 70" % (bawah_70))

else:
    print("Kamu tidak lulus")