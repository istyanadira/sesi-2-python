import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('data_penduduk/Data_Penduduk.xlsx')
q1 = df['Penghasilan_Per_Bulan'].quantile(0.25)
q2 = df['Penghasilan_Per_Bulan'].quantile(0.5)
q3 = df['Penghasilan_Per_Bulan'].quantile(0.75)

def kategorikan_penghasilan(penghasilan):
    if penghasilan < q1:
        return 'Sangat Rendah'
    elif q1 <= penghasilan < q2:
        return 'Rendah'
    elif q2 <= penghasilan < q3:
        return 'Menengah'
    else:
        return 'Tinggi'
    
df['Kategori_Penghasilan'] = df['Penghasilan_Per_Bulan'].apply(kategorikan_penghasilan)
kategori_penghasilan = df['Kategori_Penghasilan'].value_counts()
plt.pie(kategori_penghasilan, labels=kategori_penghasilan.index, autopct='%1.1f%%', startangle=140)
plt.title('Persentase Kategori Penghasilan Penduduk')
plt.axis('equal')
plt.show()