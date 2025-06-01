import pandas as pd

file_path = '40_baris_dengan_total.xlsx'
xls = pd.ExcelFile(file_path)
df = xls.parse('Sheet1')

rekap_penjualan = df.groupby('Kategori')['Total Harga'].sum().reset_index()
rekap_penjualan_columns = ['Kategori', 'Total Pendapatan']

output_path = 'rekap_penjualan_per_kategori.xlsx'
rekap_penjualan.to_excel(output_path, index=False)

print(f"File disimpan sebagai: {output_path}")