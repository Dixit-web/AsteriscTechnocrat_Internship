import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder


# Load the dataset
data = pd.read_csv('C:/Users/Shantanu/Downloads/INR=X.csv')
print(data.columns)
target_column = data['Date']
label_encoder = LabelEncoder()

# Fit label encoder on target column and transform the values
target_encoded = label_encoder.fit_transform(target_column)

# Replace the original target column with the encoded values
data['Date'] = target_encoded


# Prepare the data
X = data[['Open', 'High', 'Low','Close','Adj Close','Volume']]  # Replace with actual feature names from your dataset
y = data['Date']  # Replace 'target' with the actual target variable

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create the model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

# Make predictions
predictions = model.predict(X_test)

# Visualize the results
plt.figure(figsize=(10, 6))
plt.scatter(y_test, predictions, color='blue')
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], color='red', linestyle='--')
plt.xlabel('Actual')
plt.ylabel('Predicted')
plt.title('Actual vs Predicted Stock Prices')
plt.show()
