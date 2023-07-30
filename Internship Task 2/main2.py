#C:/Users/Shantanu/PycharmProjects/Internship Task 2/transformed_data.csv
import pandas as pd
import matplotlib.pyplot as plt

# Load the COVID-19 dataset
data = pd.read_csv('C:/Users/Shantanu/PycharmProjects/Internship Task 2/transformed_data.csv')

# Check the column names in the dataset
print(data.columns)

# Ensure the column names match the ones in your dataset
X = data[['DATE', 'TC', 'TD', 'STI', 'POP', 'GDPCAP']].copy()

# Perform data analysis and visualization
# ...

# Calculate the total cases, total deaths, and total recovered
total_cases = X['TC'].sum()
total_deaths = X['TD'].sum()
total_recovered = X['STI'].sum()

# Create a pie chart
labels = ['Total Cases', 'Total Deaths', 'Total Recovered']
sizes = [total_cases, total_deaths, total_recovered]
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
plt.axis('equal')
plt.title('COVID-19 Impact')
plt.show()
