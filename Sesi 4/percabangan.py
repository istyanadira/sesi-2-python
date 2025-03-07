nilai = int(input("Masukkan nilai: "))
grade = 'E'

if nilai >= 85:
    grade = 'A'
if nilai >= 75:
    grade = 'B'
if nilai >= 65:
    grade = 'C'
if nilai >= 55:
    grade = 'D'

print("Grade Anda adalah %s" %grade)    