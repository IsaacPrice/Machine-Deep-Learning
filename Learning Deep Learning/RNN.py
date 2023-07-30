import pandas as pd
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, SimpleRNN

# Load the data
df = pd.read_csv('Salary_Data.csv')

# Create the dummy variables
df = pd.get_dummies(df, drop_first=True)

# Drop nan values
df = df.dropna()

# Split the data into X and y
X = df.iloc[:, :-1].values
y = df.iloc[:, -1].values

# Scale the data
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Split the data into train and test
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y)

# Assume input data is of shape (batch_size, timesteps, input_dim)
input_dim = X_train.shape[1]
timesteps = 1
batch_size = 32

# Build the model
model = Sequential()

# Add the layers
model.add(SimpleRNN(100, input_shape=(timesteps, input_dim)))
model.add(Dense(10, activation='softmax'))

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(X_train, y_train, epochs=100, batch_size=batch_size)

# Evaluate the model
print(model.evaluate(X_test, y_test))