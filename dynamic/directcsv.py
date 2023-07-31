import os
import mimetypes
import argparse
import csv
import subprocess
import pandas as pd
import numpy as np
import joblib
from pyfiglet import Figlet
import warnings
from sklearn.exceptions import DataConversionWarning


warnings.filterwarnings(action='ignore', category=UserWarning)

# Create argument parser
parser = argparse.ArgumentParser(description='Process CSV file.')
parser.add_argument('filepath', type=str, help='Path to the CSV file')

# Parse arguments
args = parser.parse_args()

# Define helper function to verify file type based on extension
def check_file(file_path, expected_ext):
    if not os.path.isfile(file_path):
        print(f"Error: File {file_path} does not exist.")
        return False
    mimetype = mimetypes.guess_type(file_path)[0]
    if mimetype is None:
        print(f"Error: Unable to determine the type of file {file_path}.")
        return False
    ext = mimetypes.guess_extension(mimetype)
    if ext != expected_ext:
        print(f"Error: File {file_path} is not of expected type {expected_ext}.")
        return False
    return True

# Check if file is of expected type
if not check_file(args.filepath, ".csv"):
    exit()

# Load CSV data
data = pd.read_csv(args.filepath, header=None)

# Convert DataFrame to numpy array
data = data.to_numpy()

# Load the models
malisnot_model = joblib.load("malisnot.joblib")
maltype_model = joblib.load("rf_maltype.joblib")
trojan_family_model = joblib.load("trojan_family.joblib")
spyware_family_model = joblib.load("spyware_family.joblib")
ransom_family_model = joblib.load("ransom_family.joblib")

# Get probabilities for each class
malisnot_proba = malisnot_model.predict_proba(data)
malisnot_prediction = malisnot_model.predict(data)

maltype_proba = maltype_model.predict_proba(data)
maltype_prediction = maltype_model.predict(data)

trojan_family_proba = trojan_family_model.predict_proba(data)
spyware_family_proba = spyware_family_model.predict_proba(data)
ransom_family_proba = ransom_family_model.predict_proba(data)



# Define malware types and families
malware_types = {0: "Trojan", 1: "Spyware", 2: "Ransomware"}
trojan_families = {0: "Emotet", 1: "Reconyc", 2: "Refroso", 3: "Scar", 4: "Zeus"}
spyware_families = {0: "180solutions", 1: "CWS", 2: "Gator", 3: "TIBS", 4: "Transponder"}
ransom_families = {0: "Ako", 1: "Conti", 2: "Maze", 3: "Pysa", 4: "Shade"}

# Check the probability of being malicious or benign
if 0.45 <= malisnot_proba[0][1] <= 0.55:
    print("****Probability of being Malicious: {:.2f}, Probability of being Non-malicious: {:.2f}****\n****Probability is between 0.45-0.55. Maldives is uncertain if it is malicious or non-malicious****".format(malisnot_proba[0][1], malisnot_proba[0][0]))
else:
    if malisnot_prediction[0] == 1: 
        print("****Probability of being Malicious: {:.2f}, Probability of being Non-malicious: {:.2f}****\n****Conclusion: Malicious****".format(malisnot_proba[0][1], malisnot_proba[0][0]))
        mal_type = malware_types[maltype_prediction[0]]
        if mal_type == "Trojan":
            family_prediction = trojan_family_model.predict(data)
            print("****Possible Malware Type: Trojan, Probability: {:.2f}****".format(maltype_proba[0][0]))
            print("****Possible Trojan Family: {}, Probability: {:.2f}****".format(trojan_families[family_prediction[0]], trojan_family_proba[0][family_prediction[0]]))
        elif mal_type == "Spyware":
            family_prediction = spyware_family_model.predict(data)
            print("****Possible Malware Type: Spyware, Probability: {:.2f}****".format(maltype_proba[0][1]))
            print("****Possible Spyware Family: {}, Probability: {:.2f}****".format(spyware_families[family_prediction[0]], spyware_family_proba[0][family_prediction[0]]))
        elif mal_type == "Ransomware":
            family_prediction = ransom_family_model.predict(data)
            print("****Possible Malware type: Ransomware, Probability: {:.2f}****".format(maltype_proba[0][2]))
            print("****Possible Ransomware Family: {}, Probability: {:.2f}****".format(ransom_families[family_prediction[0]], ransom_family_proba[0][family_prediction[0]]))
    else:
        print("****Probability of being Malicious: {:.2f}, Probability of being Non-malicious: {:.2f}****\n****Conclusion: Non-malicious****".format(malisnot_proba[0][1], malisnot_proba[0][0]))

