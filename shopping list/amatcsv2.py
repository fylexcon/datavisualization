import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np  

df=pd.read_csv('shopping_list.csv')
df['Fiyat']=df['Fiyat'].astype(float)

def miktar_to_number(miktar):
    try:
        if 'kg' in miktar:
            return float(miktar.replace('kg', '').strip()) 
        elif 'lt' in miktar:
            return float(miktar.replace('lt', '').strip()) 
        elif 'g' in miktar:
            return float(miktar.replace('g', '').strip()) / 1000
        elif 'ml' in miktar:
            return float(miktar.replace('ml', '').strip()) / 1000
        else:
            return float(miktar.strip())
    except:
        return miktar

df['Miktar']=df['Miktar'].apply(miktar_to_number)
df['Toplam fiyat']=df['Fiyat']*df['Miktar']
df.to_csv('alisveris_listesi.csv',index=False,encoding='utf-8-sig')



# 1 Gün-Harcama miktarı Bar


plt.figure()

plt.bar(df['Gün'],df['Toplam fiyat'])
plt.title('Günlük Satış')
plt.xlabel('Gün')
plt.ylabel('Harcama miktarı')
plt.tight_layout()
plt.show()


# 2 Kategori-Harcama miktarı Pİe

plt.figure()
kategori_grouped = df.groupby('Kategori')['Toplam fiyat'].sum()
plt.pie(kategori_grouped, labels=kategori_grouped.index, autopct='%1.1f%%')
plt.title('Kategoriye Göre Harcama Miktarı')
plt.tight_layout()
plt.legend()
plt.show()




# 3 Ürün-Harcama Scatter

plt.figure()
colors = plt.cm.rainbow(np.linspace(0, 1, len(df['Ürün'])))
plt.scatter(df['Ürün'], df['Toplam fiyat'], c=colors)
plt.title('Ürünlere Göre Harcama Miktarı')
plt.xlabel('Ürün')
plt.ylabel('Harcama Miktarı')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()



# 4 Ürün Harcama Histogram


plt.figure()
plt.hist(df['Toplam fiyat'],bins=10,color='orange',edgecolor='black',width=0.7)
plt.title('Harcama Miktarı Histogram Grafiği')
plt.xlabel('Harcama Miktarı')
plt.ylabel('Frekans')
plt.tight_layout()
plt.show()

# 5 Ürün Fiyat Boxplot
plt.figure()
plt.boxplot(df['Fiyat'])
plt.title("Ürün Fiyatları Boxplot")
plt.ylabel("Fiyat (₺)")
plt.show()
