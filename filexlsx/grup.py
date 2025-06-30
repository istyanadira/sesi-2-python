import pandas as pd

def updateScore(score):
    if score >= 80:
        return score + 5
    elif score < 70:
        return score + (10 if score < 75 else 5)
    elif score < 60:
        return score + (10 if score < 65 else 5)
    elif score < 50:
        return score + (10 if score < 75 else 5)
    else:
        return score + (20.25 if score < 65 else 17.1)

# Fungsi untuk memberi grade
def grade(score):
    if score >= 85:
        return "A"
    elif score >= 75:
        return "B"
    elif score >= 65:
        return "C"
    else:
        return "D"

# Membaca file Excel
score = pd.read_excel("filexlsx/data-score.xlsx", sheet_name="TI24E")

# Buat kolom New Score dan Grade
score["New Score"] = score["Score"].apply(updateScore)
score["Grade"] = score["New Score"].apply(grade)

# Hitung jumlah masing-masing Grade
grade_counts = score["Grade"].value_counts().reindex(["A", "B", "C", "D"], fill_value=0)

# Tampilkan hasil
print("Jumlah Mahasiswa per Nilai:")
print(grade_counts)

# Simpan ke Excel (opsional)
grade_counts.to_excel("filexlsx/rekap-nilai.xlsx")

