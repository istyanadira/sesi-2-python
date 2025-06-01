import pandas as pd

file_path = '40_baris_dengan_total.xlsx'
xls = pd.ExcelFile(file_path)

df = xls.parse('Sheet1')

df_sorted = df.sort_values(by='Total Harga', ascending=False)
output_path = 'penjualan_terurut.xlsx'
df_sorted.to_excel(output_path, index=False)
print(f"File disimpan sebagai: {output_path}")