import pandas as pd
import numpy as np
import tkinter as tk
from tkinter import ttk, messagebox
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.utils import to_categorical

# Load the heart disease dataset
try:
    cleveland = pd.read_csv(
        'D:\_NUST\project1\capstone\heartfile.csv', na_values='?')
except FileNotFoundError:
    messagebox.showerror("Error", "Dataset file not found.")

# Drop rows with missing values
cleveland = cleveland.dropna()

# Ensure target variable is binary (0 or 1)
cleveland['target'] = cleveland['target'].apply(lambda x: 1 if x > 0 else 0)

# Split the dataset into features (X) and target variable (y)
X = cleveland.drop('target', axis=1)
y = cleveland['target']

# Feature scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Convert labels to categorical
y_categorical = to_categorical(y, num_classes=2)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y_categorical, test_size=0.2, random_state=42)

# Create a simple neural network model
model = Sequential()
model.add(Dense(16, input_dim=X_scaled.shape[1], activation='relu'))
model.add(Dropout(0.25))
model.add(Dense(8, activation='relu'))
model.add(Dropout(0.25))
model.add(Dense(2, activation='softmax'))

# Compile the model
adam = Adam(learning_rate=0.001)
model.compile(loss='categorical_crossentropy',
              optimizer=adam, metrics=['accuracy'])

# Train the model
model.fit(X_train, y_train, epochs=50, batch_size=10, verbose=0)

# Evaluate the model on the test set
y_pred_prob = model.predict(X_test)
y_pred = np.argmax(y_pred_prob, axis=1)
y_test_class = np.argmax(y_test, axis=1)

# Calculate accuracy
accuracy = accuracy_score(y_test_class, y_pred)
print(f'Test Accuracy: {accuracy}')

# The rest of your GUI code...

# GUI Function for Predicting Heart Disease


def predict_heart_disease():
    # Extract user input
    user_data = []
    for entry in entries:
        try:
            user_data.append(float(entry.get()))
        except ValueError:
            messagebox.showerror(
                "Error", "Please enter valid numerical values.")
            return

    # Feature scaling for user input
    scaled_user_data = scaler.transform([user_data])

    # Make prediction
    prediction_prob = model.predict(scaled_user_data)
    prediction = np.argmax(prediction_prob)

    # Display result
    result_label.config(
        text=f"Prediction: {'Positive' if prediction == 1 else 'Negative'}")


# Create Tkinter window
root = tk.Tk()
root.title("Heart Disease Prediction App")

root.geometry("800x800")  # Set the window size

# Add a background color
root.configure(bg='lightgray')  # Light gray color

# Add a topic label
topic_label = ttk.Label(root, text="Heart Disease Predictor", font=(
    'Helvetica', 25, 'bold'), background='#f0f0f0')
topic_label.grid(row=0, column=1, columnspan=2, pady=10)

# Create entry widgets for user input
entries = []
for i, column in enumerate(cleveland.columns[:-1]):
    label = ttk.Label(root, text=f"{column}:", font=('Segoe Script bold', 14),)
    label.grid(row=i+1, column=1, padx=10, pady=5)
    entry = ttk.Entry(root, font=('Segoe Script bold', 14))
    entry.grid(row=i+1, column=2, padx=10, pady=5)
    entries.append(entry)

# Button to predict heart disease
predict_button = ttk.Button(
    root, text="         Predict       ", command=predict_heart_disease)
predict_button.grid(
    row=len(cleveland.columns[:16]) + 1, column=2, columnspan=2, pady=10)


# Label to display prediction result
result_label = ttk.Label(root, text="")
result_label.grid(
    row=len(cleveland.columns[:14]) + 2, column=2, columnspan=2, pady=10)

# Run the Tkinter event loop
root.mainloop()
