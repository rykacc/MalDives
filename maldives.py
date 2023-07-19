import csv
import subprocess
import pandas as pd
import numpy as np
import joblib
from pyfiglet import Figlet
import warnings
from sklearn.exceptions import DataConversionWarning

warnings.filterwarnings(action='ignore', category=UserWarning)

# create a Figlet object
f = Figlet(font='smslant')

# print a banner when the script starts
print(f.renderText('MalDives'))

def extract_number(text):
    return float(text.split(":")[-1].strip())

scripts = ["pslist.py", "dlllist.py", "handles.py", "ldrmodule.py", "malfind.py", "psxview.py", "modules.py", "svcscan.py", "callbacks.py"]
results = []

for script in scripts:
    result = subprocess.run(["python", script], stdout=subprocess.PIPE, text=True)
    for line in result.stdout.split("\n"):
        if ":" in line:
            results.append(extract_number(line))

with open('output.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(results)
    
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

# Get probabilities for each class
malisnot_proba = malisnot_model.predict_proba(data)
malisnot_prediction = malisnot_model.predict(data)  # Added this line
maltype_proba = maltype_model.predict_proba(data)

if malisnot_prediction[0] == 1:  # Change here assuming that 1 represents 'Malicious' 
    print("****Probability of being Malicious: {:.2f}, Probability of being Non-malicious: {:.2f}****\n****Conclusion: Malicious****".format(malisnot_proba[0][1], malisnot_proba[0][0]))
    
    maltype_prediction = maltype_model.predict(data)
    
    if maltype_prediction[0] == "Trojan":
        family_prediction = trojan_family_model.predict(data)
        print("****Possible Malware Type: Trojan, Probability: {:.2f}****".format(maltype_proba[0][1]))
        print("****Possible Trojan Family: {}, Probability: {:.2f}****".format(family_prediction[0], trojan_family_proba[0][1]))
    elif maltype_prediction[0] == "Spyware":
        family_prediction = spyware_family_model.predict(data)
        print("****Possible Maltype Type: Spyware, Probability: {:.2f}****".format(maltype_proba[0][2]))
        print("****Possible Spyware Family: {}, Probability: {:.2f}****".format(family_prediction[0], spyware_family_proba[0][1]))
    elif maltype_prediction[0] == "Ransomware":
        family_prediction = ransom_family_model.predict(data)
        print("Possible Malware type: Ransomware, Probability: {:.2f}****".format(maltype_proba[0][3]))
        print("****Possible Ransomware Family: {}, Probability: {:.2f}".format(family_prediction[0], ransom_family_proba[0][1]))
else:
    print("****Probability of being Malicious: {:.2f}, Probability of being Non-malicious: {:.2f}****\n****Conclusion: Non-malicious****".format(malisnot_proba[0][1], malisnot_proba[0][0]))

