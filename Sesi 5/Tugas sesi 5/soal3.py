nilai = int(input("Masukkan nilai: "))

if nilai >= 80 and nilai <= 100:
    print("Grade A")
elif nilai >= 70 and nilai <= 79:
    print("Grade B")
elif nilai >= 60 and nilai <= 69:
    print("Grade C")
elif nilai >= 50 and nilai <= 59:
    print("Grade D")
else:
    print("Grade E")