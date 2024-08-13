
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Analyze the distribution of key features
plt.figure(figsize=(15, 10))
data[['tenure', 'MonthlyCharges', 'TotalCharges']].hist(bins=30, edgecolor='black', color='skyblue', layout=(2, 2), figsize=(10, 8))
plt.tight_layout()

# 2. Visualize the correlation between features and the target variable (Churn)
correlation = data.corr()
plt.figure(figsize=(12, 8))
sns.heatmap(correlation, annot=True, fmt=".2f", cmap='coolwarm')
plt.title('Correlation Matrix')

# 3. Identify any potential outliers or patterns using boxplots
plt.figure(figsize=(15, 10))
sns.boxplot(x='Churn', y='MonthlyCharges', data=data)
plt.title('MonthlyCharges vs Churn')

sns.boxplot(x='Churn', y='TotalCharges', data=data)
plt.title('TotalCharges vs Churn')
