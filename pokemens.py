import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pokemon_df = pd.read_csv("./Pokemon.csv")
#print(pokemon_df[pokemon_df['Name'] == 'Bulbasaur'])
#print(pokemon_df[pokemon_df['Legendary'] == True])
#print(pokemon_df[pokemon_df['Type 1'] == 'Electric'])
#print(pokemon_df.select_dtypes(include=numbers).mean())
#print(pokemon_df.describe().astype(int))
pokemon_stats = pokemon_df.drop(['Type 1', 'Type 2', '#', 'Legendary', 'Name', 'Total', 'Generation'], axis=1)

plt.rcParams['figure.dpi'] = 150
sns.set_theme(style="whitegrid")

#plt.figure(figsize=(12,5))
plt.figure(figsize=(8,8))
#sns.countplot(data=pokemon_df, x='Type 2', order=pokemon_df['Type 2'].value_counts().index, palette='Set2')
#sns.distplot(pokemon_df.Attack, kde=False)
#sns.boxplot(data=pokemon_df, x='Type 1', y='Attack')
#sns.boxplot(x=pokemon_df.Attack)
sns.boxplot(data=pokemon_stats)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


print(pokemon_df[pokemon_df['HP'] > 225])
print(pokemon_df[pokemon_df['HP'] < 10])
print(pokemon_df[pokemon_df['Defense'] > 200])
print(pokemon_df[pokemon_df['Sp. Def'] > 200])