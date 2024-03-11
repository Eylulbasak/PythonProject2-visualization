import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
df = sns.load_dataset('tips')
df.head()
sns.countplot(x=df['sex'], data=df)
plt.show()

sns.boxplot(x=df['total_bill'])
plt.show()

df['total_bill'].hist()
plt.show()