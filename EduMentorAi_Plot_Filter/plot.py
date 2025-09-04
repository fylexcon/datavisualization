import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path


data = Path(__file__).parent / "EduMentorAI_Plot_Filter.csv"
df = pd.read_csv(data)



output_dir = Path(__file__).parent / "outputs"
output_dir.mkdir(exist_ok=True)

sns.boxplot(data=df[['Matematik', 'Fen', 'Turkce', 'Sosyal']])
plt.title('Box Plot of Student Scores')
plt.xlabel('Subjects')
plt.ylabel('Scores')
plt.savefig(output_dir / "boxscores.png", dpi=150)
plt.show()






fig,axes=plt.subplots(1,2,figsize=(12,6))

df[['Matematik','Fen','Turkce','Sosyal']].mean().plot(kind='hist',bins=15,alpha=0.7,ax=axes[0],color='blue')
axes[0].set_title('Histogram of Student Scores')
axes[0].set_xlabel('Scores')

sns.kdeplot(data=df[['Matematik','Fen','Turkce','Sosyal']],ax=axes[1],fill=True)
axes[1].set_title('Density Plot of Student Scores')
axes[1].set_xlabel('Scores')
plt.tight_layout()
plt.savefig(output_dir / "hist_density_scores.png", dpi=150)
plt.show()


#heatmap

plt.figure(figsize=(15,10))
sns.heatmap(df[['Matematik','Fen','Turkce','Sosyal']],annot=True,cmap='coolwarm')
plt.title('Heatmap of Student Scores')
plt.xlabel('Subjects')
plt.ylabel('Students')
plt.savefig(output_dir / "heatmap_scores.png", dpi=150)
plt.show()