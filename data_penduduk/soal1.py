import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('data_penduduk/Data_Penduduk.xlsx')
profesi = df['Profesi'].value_counts()
plt.pie(profesi, labels=profesi.index, autopct='%1.1f%%', startangle=140)
plt.title('Persentase Profesi Penduduk')
plt.axis('equal')
plt.show()