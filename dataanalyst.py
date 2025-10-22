import pandas as pd
#import seaborn as sns
#import matplotlib.pyplot as plt
import numpy as np

print(pd.__version__)

train = pd.read_csv('train.csv'); # data latih
test = pd.read_csv('test.csv'); # data uji

print(train)
print(test)









#data = {
#    'nama_produk': ['Sabun Mandi A','Sampo X','Snack Ring','Minuman Y','Snack Keju','Kopi Hitam','Air Mineral','Pasta Gigi Z',
#                   'Snack Ring','Sampo X','Kopi Hitam','Snack Keju','Minuman Y','Air Mineral','Pasta Gigi Z'],
#    'kategori': ['Kebutuhan Rumah','Kebutuhan Rumah','Makanan','Makanan','Makanan','Makanan','Makanan','Kebutuhan Rumah',
#                 'Makanan','Kebutuhan Rumah','Minuman','Makanan','Minuman','Minuman','Kebutuhan Rumah'],
#    'harga': [10000,35000,13000,10000,9500,15000,5000,18000,15000,None,15000,19500,10000,5000,18000],
#    'jumlah_terjual': [150,90,300,400,250,180,600,120,310,100,None,250,400,1000,110],
#    'kota': ['jakarta','bandung','jakarta','surabaya','jakarta','bandung','surabaya','jakarta','Jakarta','bandung','Surabaya','jakarta','surabaya','surabaya','jakarta'],
#    'tanggal': ['2024-01-05','2024-01-07','2024-01-08','2024-01-09','2024-01-10','2024-01-11','2024-01-12','2024-01-13',
#                '2024-01-14','2024-01-15','2024-01-16','2024-01-17','2024-01-18','2024-01-19','2024-01-20']
#}

# Buat DataFrame
#df = pd.DataFrame(data)

#print(df.head())
#print(df.info(5))

#print(df['harga'].mode())
#print(df['harga'].mean())      # Rata-rata
#print(df['harga'].median())

#print(df.isnull().sum())     # Missing values
#print(df.duplicated().sum())

#df.drop_duplicates(inplace=True)
#df

#df['kota'] = df['kota'].str.title()  # “jakarta” → “Jakarta”
#df

#sns.countplot(x='kategori', data=df)
#plt.title('Jumlah Produk per Kategori')
#plt.show()