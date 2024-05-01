import seaborn as sns
import matplotlib.pyplot as plt

# Set the Seaborn style
sns.set_style("whitegrid")

# Load a sample dataset
df = sns.load_dataset('iris')

# Scatter Plot
plt.figure(figsize=(8, 6))
sns.scatterplot(x='sepal_length', y='sepal_width', data=df)
plt.title('Scatter Plot')
plt.show()

# Line Plot
plt.figure(figsize=(8, 6))
sns.lineplot(x='sepal_length', y='petal_length', data=df)
plt.title('Line Plot')
plt.show()

# Bar Plot
plt.figure(figsize=(8, 6))
sns.barplot(x='species', y='petal_width', data=df)
plt.title('Bar Plot')
plt.show()

# Histogram
plt.figure(figsize=(8, 6))
sns.histplot(data=df, x='sepal_length', bins=20)
plt.title('Histogram')
plt.show()

# Box Plot
plt.figure(figsize=(8, 6))
sns.boxplot(x='species', y='petal_length', data=df)
plt.title('Box Plot')
plt.show()

# Violin Plot
plt.figure(figsize=(8, 6))
sns.violinplot(x='species', y='sepal_width', data=df)
plt.title('Violin Plot')
plt.show()

# Heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(data=df.corr(), annot=True, cmap='coolwarm')
plt.title('Heatmap')
plt.show()

# Pairplot
plt.figure(figsize=(8, 6))
sns.pairplot(df)
plt.title('Pairplot')
plt.show()

# Jointplot
sns.jointplot(x='petal_length', y='petal_width', data=df, kind='scatter')
plt.title('Jointplot')
plt.show()
