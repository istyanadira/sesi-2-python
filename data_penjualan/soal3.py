import pandas as pd

data = pd.read_excel('data_penjualan.xlsx')
data_elektronik = data[data['Kategori'] == 'Elektronik'].head(40)

data_elektronik.to_excel('elektronik.xlsx', index=False)
print("File elektronik.xlsx berhasil dibuat.")