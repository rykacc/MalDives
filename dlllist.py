import re

with open('extracted_dlllist.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Initialize counters
ndlls = 0
nprocs = 0

# Regex to match the lines with process info
regex = re.compile(r'^0x')

for line in lines:
    if 'Command line' in line:
        nprocs += 1
    elif regex.search(line):
        ndlls += 1

avg_dlls_per_proc = ndlls / nprocs if nprocs != 0 else 0

print(f"dlllist.ndlls: {ndlls}")
print(f"dlllist.avg_dlls_per_proc: {avg_dlls_per_proc}")
