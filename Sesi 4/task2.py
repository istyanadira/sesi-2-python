nomer = int(input("Masukkan nomer: "))
if nomer == 0:
    bil = "nol"
elif nomer >= 0:
    bil = "positif"
elif nomer <= 0:
    bil = "negatif"

print(nomer, "adalah bilangan", bil)