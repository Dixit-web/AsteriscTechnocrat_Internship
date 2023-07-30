import pandas as pd

# Load the COVID-19 dataset
from matplotlib import pyplot as plt

data = pd.read_csv('C:/Users/Shantanu/PycharmProjects/Internship Task 2/transformed_data.csv')

# Check the column names in the dataset
print(data.columns)

# Ensure the column name matches the one in your dataset
X = data[['DATE', 'TC', 'TD', 'STI', 'POP', 'GDPCAP']]  # Replace with the actual column names from your dataset

# Perform data analysis and visualization
X = data[['DATE', 'TC', 'TD', 'STI', 'POP', 'GDPCAP']]

# Convert the 'DATE' column to datetime format
X['DATE'] = pd.to_datetime(X['DATE'])

# Set the 'DATE' column as the index
X.set_index('DATE', inplace=True)

# Plot the total confirmed cases ('TC') over time
plt.figure(figsize=(10, 6))
plt.plot(X.index, X['TC'])
plt.xlabel('Date')
plt.ylabel('Total Confirmed Cases')
plt.title('COVID-19 Total Confirmed Cases Over Time')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()





#C:\Users\Shantanu\PycharmProjects\Internship Task 2\transformed_data.csv