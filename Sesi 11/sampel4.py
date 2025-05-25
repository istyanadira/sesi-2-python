def konversi_suhu(suhu, dari = "C", ke = "R, F, K"):
    if ke == "R":
        return (suhu * 4/5)
    elif ke == "F":
        return (suhu * 9/5) + 32
    elif ke == "K":
        return (suhu + 273.15)
    else:
        raise ValueError("Satuan tidak valid. Gunakan 'C' untuk Celsius atau 'F' untuk Fahrenheit.")

print("Konversinya dari 100 C adalah", konversi_suhu(100, "C", "K"))
