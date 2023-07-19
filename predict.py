import pandas as pd
import numpy as np
from keras.models import load_model
import joblib

# Load CSV data
data = pd.read_csv("output.csv", header=None)

# Convert DataFrame to numpy array
data = data.to_numpy()

# Reshape the data to match the input shape required by your CNN model
data_3d = np.expand_dims(data, axis=2)

# Load the models
malisnot_model = load_model("malisnot.h5")
maltype_model = joblib.load("rf_maltype.joblib")
trojan_family_model = joblib.load("trojan_family.joblib")
spyware_family_model = joblib.load("spyware_family.joblib")
ransom_family_model = joblib.load("ransom_family.joblib")

# Prediction for CNN model
malisnot_prediction = malisnot_model.predict(data_3d)

if malisnot_prediction[0][0] > 0.5:  # assuming the model output is a probability
    # Now we need 2D input for RandomForest models
    data_2d = np.squeeze(data_3d, axis=2)
    
    maltype_prediction = maltype_model.predict(data_2d)
    
    if maltype_prediction[0] == "Trojan":
        family_prediction = trojan_family_model.predict(data_2d)
        print("Trojan-", family_prediction)
    elif maltype_prediction[0] == "Spyware":
        family_prediction = spyware_family_model.predict(data_2d)
        print("Spyware-", family_prediction)
    elif maltype_prediction[0] == "Ransomware":
        family_prediction = ransom_family_model.predict(data_2d)
        print("Ransomware-", family_prediction)
else:
    print("Not Malicious")
