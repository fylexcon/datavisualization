import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from pathlib import Path


d=Path(__file__).parent / "EduMentorAI_Plot_Filter.csv"
df=pd.read_csv(d)
df["Sinif Düzeyi"]=df["Sinif"].str.extract('(\d)')
df["Sinif Düzeyi"]=df["Sinif Düzeyi"].astype(int)
output_dir = Path(__file__).parent / "outputs"
output_dir.mkdir(exist_ok=True)





df.groupby('Sinif')['ToplamPuan'].mean().plot(kind='bar',color='skyblue')
plt.title('Average Total Score by Class')
plt.xlabel('Class')
plt.ylabel('Average Total Score')

plt.savefig(output_dir / "avg_total_score_by_class.png", dpi=150)
plt.show()




df['DusukPuan']=df['DusukPuan'].apply(lambda x:1 if x.lower()=="evet" else 0)
df.groupby('Sinif Düzeyi')['DusukPuan'].mean().plot(kind='bar',color='salmon')
plt.title('Average Low Score by Grade')
plt.xlabel('Class')
plt.ylabel('Average Low Score')
plt.savefig(output_dir / "avg_low_score_by_class.png", dpi=150)
plt.show()



