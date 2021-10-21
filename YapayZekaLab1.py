import numpy as np
import pandas as pd
import random
# -*- coding: utf-8 -*-

# tablo açma
veri=pd.read_csv('C:/Users/furka/OneDrive/Masaüstü/lab1YapayZeka.csv',encoding='unicode_escape')
print(veri)

#sıcaklık ve nem değeri silme



sil=veri.drop(["Sicaklik","Nem"],axis=1)
print(sil)


# dataframe

d={'Gün':['G1','G2','G3','G4','G5','G6','G7','G8','G9','G10','G11','G12','G13','G14'],
   'Hava Durmu':['Güneşli','Güneşli','Kapalı','Yağmurlu','Yağmurlu','Yağmurlu','Kapalı','Güneşli','Güneşli','Yağmurlu','Güneşli','Kapalı','Kapalı','Yağmurlu'],
   'Sıcaklık':['Sıcak','Sıcak','Sıcak','Ilıman','Soğuk','Soğuk','Soğuk','Ilıman','Soğuk','Ilıman','Ilıman','Ilıman','Sıcak','Ilıman'],
   'Nem':['Yüksek','Yüksek','Yüksek','Yüksek','Normal','Normal','Normal','Yüksek','Normal','Normal','Normal','Yüksek','Normal','Yüksek'],
   'Yağış':['Seyrek','Aşırı','Seyrek','Seyrek','Seyrek','Aşırı','Aşırı','Seyrek','Seyrek','Seyrek','Aşırı','Aşırı','Seyrek','Aşırı'],
   'Oyun':['Yok','Yok','Var','Var','Var','Yok','Var','Var','Yok','Var','Var','Yok','Var','Yok']}
df=pd.DataFrame(data=d)
print(df)


print(df.info())
print(df.describe())

# (3,4) boyutunda dizi
dizi=np.array([[1,2,3,4],
               [1,2,3,4],
               [1,2,3,4]])
print(dizi)


yeniDizi=np.delete(dizi,3,axis=1)
yeniDizi1=np.delete(yeniDizi,2,axis=1)
print(yeniDizi1)

ekle1=np.array([1,2])
ekle2=np.array([1,2])
ekle3=np.array([1,2])
ekle4=np.array([1,2])
yeni1=np.vstack([yeniDizi1,ekle1])



print(yeni1)

#4.soru


matriks1 = [np.random.randn(3, 3) for _ in range(10)]
print(matriks1)

matriks2 = [np.random.randn(3, 3) for _ in range(10)]
print(matriks2)

print(np.stack((matriks1, matriks2)))
print(np.stack((matriks1, matriks1), axis=-1))

#s=np.stack((matriks1, matriks2))
#print(s)

#matriks3=np.vstack([matriks1,matriks2])
#print(matriks3)


























