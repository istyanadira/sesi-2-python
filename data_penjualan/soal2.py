import pandas as pd

data = pd.read_excel('data_penjualan.xlsx').head(40)

data['Total Harga'] = data['Jumlah'] * data['Harga Satuan']

data.to_excel('40_baris_dengan_total.xlsx', index=False)
print("File 40_baris_dengan_total.xlsx berhasil dibuat.")