import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('data_penduduk/Data_Penduduk.xlsx')
pendidikan = df['Pendidikan_Terakhir'].value_counts()
jenis_kelamin = df['Jenis_Kelamin'].value_counts()
plt.bar(pendidikan.index, pendidikan.values, color='skyblue', label='Pendidikan Terakhir')
plt.bar('jenis_kelamin', jenis_kelamin.values, color='lightgreen', label='Jenis Kelamin', alpha=0.7)
plt.xlabel('Pendidikan Terakhir & Jenis Kelamin')
plt.ylabel('Jumlah')
plt.title('Jumlah penduduk berdasarkan Pendidikan Terakhir dan Jenis Kelamin')
plt.show()