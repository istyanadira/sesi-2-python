def konversi_suhu(suhu, dari = "C", ke = "R"):
    if (dari == "C" and ke == "R"):
        return (4/5 * suhu)
    
print(konversi_suhu(100))