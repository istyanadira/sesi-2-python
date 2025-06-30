# import pandas as pd
# import matplotlib.pyplot as plt

# # Baca data rekap
# rekap = pd.read_excel("filexlsx/rekap-nilai.xlsx", index_col=0, header=None, names=["Grade", "Jumlah"])

# # Hitung total dan persentase
# rekap["Persen"] = (rekap["Jumlah"] / rekap["Jumlah"].sum()) * 100

# # Buat grafik batang
# plt.figure(figsize=(8, 5))
# bars = plt.bar(rekap.index, rekap["Persen"], color='skyblue', edgecolor='black')

# # Tambahkan label persentase di atas batang
# for bar, persen, jumlah in zip(bars, rekap["Persen"], rekap["Jumlah"]):
#     plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
#              f'{jumlah} ({persen:.1f}%)',
#              ha='center', va='bottom', fontsize=10)

# # Judul dan label
# plt.title("Distribusi Grade Mahasiswa (Persentase)", fontsize=14)
# plt.xlabel("Grade")
# plt.ylabel("Persentase (%)")
# plt.ylim(0, rekap["Persen"].max() + 10)  # Tambahkan ruang untuk teks

# plt.tight_layout()
# plt.show()

import pandas as pd

