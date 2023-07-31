from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report
from joblib import dump
import pandas as pd
import numpy as np 

# Load data
data = pd.read_csv('MalMem2022_type.csv')

# Separate features and labels
features = data.iloc[:, 1:]  # first column is the label
labels = data.iloc[:, 0]

# Encode labels using LabelEncoder
encoder = LabelEncoder()
encoded_labels = encoder.fit_transform(labels)

# Split data into training and test set
x_train, x_test, y_train, y_test = train_test_split(features, encoded_labels, test_size=0.2, random_state=42)

# Define the Random Forest model
rf = RandomForestClassifier(random_state=42)

# Define a dictionary of hyperparameters for GridSearch
param_grid = {
    'n_estimators': [500],
    'max_depth': [40],
    'min_samples_split': [10],
    'min_samples_leaf': [1],
    'bootstrap': [False]
}

# Define the GridSearchCV object
grid_search = GridSearchCV(estimator=rf, param_grid=param_grid, cv=3, verbose=2, n_jobs=-1)

# Fit the GridSearchCV object to the data
grid_search.fit(x_train, y_train)

# Print the best parameters
print(grid_search.best_params_)

# Predict on the test data
y_pred = grid_search.predict(x_test)

# Print classification report
print(classification_report(y_test, y_pred))

# Save the model
dump(grid_search.best_estimator_, 'rf_maltype.joblib') 

