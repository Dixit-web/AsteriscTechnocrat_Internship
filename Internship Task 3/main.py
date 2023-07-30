import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data = pd.read_csv('C:/Users/Shantanu/PycharmProjects/Internship Task 3/transformed_data .csv')
# Display the first few rows of the dataset
print(data.head())

# Check the column names and data types
print(data.info())
print(data.columns)

# Perform descriptive statistics
print(data.describe())
# Correlation heatmap
corr_matrix = data.corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()

plt.figure(figsize=(12, 6))
country_counts = data['Country'].value_counts().head(10)
sns.barplot(x=country_counts.index, y=country_counts.values)
plt.xlabel('COUNTRY')
plt.ylabel('Number of Billionaires')
plt.title('Top 10 Countries with the Highest Number of Billionaires')
plt.xticks(rotation=45)
plt.show()
