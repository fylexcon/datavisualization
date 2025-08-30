import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


data=pd.read_csv('matplotlib_dataset.csv')
data['Gün']=pd.to_datetime(data['Gün'])


#1 Gün-Satış Çizgi Grafiği

plt.figure()
plt.plot(data['Gün'],data['Satış'])
plt.title('Günlük Satış')
plt.xlabel('Gün')
plt.ylabel('Satış')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


#2 Müşteri-Satış Grafiği

plt.figure()
plt.scatter(data['Müşteri Sayısı'],data['Satış'])
plt.title('Müşteri Sayısına Göre Satış')
plt.xlabel('Müşteri Sayısı')
plt.ylabel('Satış')
plt.tight_layout()  
plt.show()


#3 Maliyet-Satış Grafiği

plt.figure()
plt.bar(data['Maliyet'],data['Satış'])
plt.title('Maliyete Göre Satış')
plt.xlabel('Maliyet') 
plt.ylabel('Satış')
plt.tight_layout() 
plt.show()

#4 Gün-Kategori-Müşteri Sayısı-Satış Grafiği

plt.figure()
x,y=data['Gün'],data['Müşteri Sayısı']
plt.subplot(2,1,1)
plt.bar(x,y)
plt.title('Günlük Müşteri Sayısı')
plt.xlabel('Gün')
plt.ylabel('Müşteri Sayısı')


plt.figure()
y,x=data['Satış'],data['Kategori']
plt.subplot(2,1,2)
plt.bar(x,y)
plt.title('Kategoriye Göre Satış')
plt.tight_layout()
plt.xlabel('Kategori')
plt.ylabel('Satış')


plt.show()


#5 Satış Histogram Grafiği
plt.figure()
plt.hist(data['Satış'],bins=10)
plt.title('Satış Histogram Grafiği')
plt.xlabel('Satış')
plt.ylabel('Frekans') 
plt.tight_layout()
plt.show()  