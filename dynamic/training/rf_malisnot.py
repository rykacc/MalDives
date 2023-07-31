from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
from sklearn.utils import class_weight
import joblib
import pandas as pd
import numpy as np
import os, time

# Load data
data = pd.read_csv('MalMem2022_isnot.csv')

# Separate features and labels
features = data.iloc[:, 1:]  # first column is the label
labels = data.iloc[:, 0]

# Encode labels using LabelEncoder
encoder = LabelEncoder()
encoded_labels = encoder.fit_transform(labels)

# Split data into training and test set
x_train, x_test, y_train, y_test = train_test_split(features, encoded_labels, test_size=0.2, random_state=42)

# Calculate class weights
sample_weights = class_weight.compute_sample_weight('balanced', y_train)

# Define the RandomForest model
rf_model = RandomForestClassifier(n_estimators=100, max_depth=None, min_samples_split=2, random_state=0)

# Fit the model
rf_model.fit(x_train, y_train, sample_weight=sample_weights)

# Predict on the test set
y_pred = rf_model.predict(x_test)

# Print accuracy
print("Accuracy:", accuracy_score(y_test, y_pred))

# Save the model
joblib.dump(rf_model, 'malisnot.joblib')
