import pandas as pd

file_path = 'data_penjualan.xlsx'
data = pd.read_excel(file_path)

first_five_rows = data.head()

output_file = '5_baris_pertama.xlsx'
first_five_rows.to_excel(output_file, index=False)

print(f"Data berhasil di simpan ke dalam file. {output_file}")