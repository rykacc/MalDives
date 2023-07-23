import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score, accuracy_score, confusion_matrix
import pickle

# Importing Dataset
malData = pd.read_csv("D:\\capstone\\data.csv", sep="|")

# Data Cleaning
y = malData['legitimate']
malData = malData.drop(['legitimate'], axis=1)
malData = malData.drop(['Name'], axis=1)
malData = malData.drop(['md5'], axis=1)
print("The Name and md5 variables are removed successfully")

# Dataset Splitting
X_train, X_test, y_train, y_test = train_test_split(malData, y, test_size=0.2, random_state=42)

# Create a RandomForest model
model = RandomForestClassifier(n_estimators=100)

# Train the model
model.fit(X_train, y_train)

# Accuracy on the training dataset
trainPred = model.predict(X_train)
print('Train Accuracy: %.2f' % accuracy_score(y_train, trainPred))

# Accuracy on the test dataset
y_pred = model.predict(X_test)
print('Test Accuracy: %.2f' % accuracy_score(y_test, y_pred))

# Model evaluation
print("Confusion Matrix: \n", confusion_matrix(y_test, y_pred))
print("F1 Score: \n", f1_score(y_test, y_pred))

# Save the model
with open('my_model.pkl', 'wb') as file:
    pickle.dump(model, file)
