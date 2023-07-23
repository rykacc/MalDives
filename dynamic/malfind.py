import re

with open('extracted_malfind.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Initialize counters
ninjections = 0
commit_charge = 0
protection = 0

# Dictionary to hold the frequency of each injection
injection_counts = {}

# Regex to match the lines with process info and hexadecimal content
regex_process = re.compile(r'Process: .* Pid: .* Address: .*')
regex_hex_content = re.compile(r'^0x[0-9a-fA-F]{8}  (([0-9a-fA-F]{2} ){16})')
regex_flags = re.compile(r'Flags: .*')

# Variables to hold the current injection
current_injection = []
in_injection = False

for line in lines:
    if regex_process.search(line):
        ninjections += 1
        # If we were in an injection, add it to the dictionary of injection counts
        if in_injection:
            injection_str = ''.join(current_injection)
            if injection_str in injection_counts:
                injection_counts[injection_str] += 1
            else:
                injection_counts[injection_str] = 1
            current_injection = []
        in_injection = True
    elif regex_flags.search(line):
        if 'CommitCharge' in line:
            commit_charge += int(line.split('CommitCharge: ')[1].split(',')[0])
        if 'Protection' in line:
            protection += int(line.split('Protection: ')[1].split(',')[0])
    elif in_injection:
        hex_match = regex_hex_content.search(line)
        if hex_match:
            current_injection.append(hex_match.group(1))

# Count the number of unique injections that appear only once
unique_injections_count = list(injection_counts.values()).count(1)

print(f"malfind.ninjections: {ninjections}")
print(f"malfind.commit_charge: {commit_charge}")
print(f"malfind.protection: {protection}")
print(f"malfind.unique_injections: {unique_injections_count}")
