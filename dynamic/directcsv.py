import csv
import subprocess
import pandas as pd
import numpy as np
import joblib
from pyfiglet import Figlet
import warnings
from sklearn.exceptions import DataConversionWarning

warnings.filterwarnings(action='ignore', category=UserWarning)
# Load CSV data
data = pd.read_csv("output.csv", header=None)

# Convert DataFrame to numpy array
data = data.to_numpy()

# Load the models
malisnot_model = joblib.load("malisnot.joblib")
maltype_model = joblib.load("rf_maltype.joblib")
trojan_family_model = joblib.load("trojan_family.joblib")
spyware_family_model = joblib.load("spyware_family.joblib")
ransom_family_model = joblib.load("ransom_family.joblib")

# Malware type to string mapping
malware_type_dict = {0: 'Trojan', 1: 'Spyware', 2: 'Ransomware'}

# Malware family to string mapping
trojan_family_dict = {0: 'Emotet', 1: 'Reconyc', 2: 'Refroso', 3: 'Scar', 4: 'Zeus'}
spyware_family_dict = {0: '180solutions', 1: 'CWS', 2: 'Gator', 3: 'TIBS', 4: 'Transponder'}
ransom_family_dict = {0: 'Ako', 1: 'Conti', 2: 'Maze', 3: 'Pysa', 4: 'Shade'}

# Get probabilities for each class
malisnot_proba = malisnot_model.predict_proba(data)
malisnot_prediction = malisnot_model.predict(data)  
maltype_proba = maltype_model.predict_proba(data)
trojan_family_proba = trojan_family_model.predict_proba(data)
spyware_family_proba = spyware_family_model.predict_proba(data)
ransom_family_proba = ransom_family_model.predict_proba(data)


if malisnot_prediction[0] == 1:
    print("****Probability of being Malicious: {:.2f}, Probability of being Non-malicious: {:.2f}****\n****Conclusion: Malicious****".format(malisnot_proba[0][1], malisnot_proba[0][0]))
    
    maltype_prediction = maltype_model.predict(data)
    maltype_str = malware_type_dict.get(maltype_prediction[0], "Unknown")
    
    if maltype_str == "Trojan":
        family_prediction = trojan_family_model.predict(data)
        family_str = trojan_family_dict.get(family_prediction[0], "Unknown")
        print("****Possible Malware Type: Trojan, Probability: {:.2f}****".format(maltype_proba[0][0]))
        print("****Possible Trojan Family: {}, Probability: {:.2f}****".format(family_str, trojan_family_proba[0][family_prediction[0]]))
    elif maltype_str == "Spyware":
        family_prediction = spyware_family_model.predict(data)
        family_str = spyware_family_dict.get(family_prediction[0], "Unknown")
        print("****Possible Malware Type: Spyware, Probability: {:.2f}****".format(maltype_proba[0][1]))
        print("****Possible Spyware Family: {}, Probability: {:.2f}****".format(family_str, spyware_family_proba[0][family_prediction[0]]))
    elif maltype_str == "Ransomware":
        family_prediction = ransom_family_model.predict(data)
        family_str = ransom_family_dict.get(family_prediction[0], "Unknown")
        print("****Possible Malware Type: Ransomware, Probability: {:.2f}****".format(maltype_proba[0][2]))
        print("****Possible Ransomware Family: {}, Probability: {:.2f}****".format(family_str, ransom_family_proba[0][family_prediction[0]]))
else:
    print("****Probability of being Malicious: {:.2f}, Probability of being Non-malicious: {:.2f}****\n****Conclusion: Non-malicious****".format(malisnot_proba[0][1], malisnot_proba[0][0]))
