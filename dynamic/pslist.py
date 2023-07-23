import re

with open('extracted_pslist.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Initialize counters
nproc = 0
ppid_set = set()
total_threads = 0
nprocs64bit = 0
total_handlers = 0

# Regex to match the lines with process info
regex = re.compile(r'\d+\s+\d+\s+\d+\s+\d+')

for line in lines:
    if regex.search(line):
        parts = line.split()
        nproc += 1
        ppid_set.add(parts[3])
        total_threads += int(parts[4])
        total_handlers += int(parts[5]) if parts[5] != '------' else 0
        nprocs64bit += 1 if parts[7] == '1' else 0

nppid = len(ppid_set)
avg_threads = total_threads / nproc if nproc != 0 else 0
avg_handlers = total_handlers / nproc if nproc != 0 else 0

print(f"pslist.nproc: {nproc}")
print(f"pslist.nppid: {nppid}")
print(f"pslist.avg_threads: {avg_threads}")
print(f"pslist.nprocs64bit: {nprocs64bit}")
print(f"pslist.avg_handlers: {avg_handlers}")