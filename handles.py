import re

with open('extracted_handles.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Initialize counters
nhandles = 0
pids = set()
nfile = 0
nevent = 0
ndesktop = 0
nkey = 0
nthread = 0
ndirectory = 0
nsemaphore = 0
ntimer = 0
nsection = 0
nmutant = 0
nport = 0

# Regex to match the lines with handle info
regex = re.compile(r'^0x')

for line in lines:
    if regex.search(line):
        parts = line.split()
        if len(parts) < 5:
            continue
        nhandles += 1
        pids.add(parts[1])
        handle_type = parts[4]
        if handle_type == 'File':
            nfile += 1
        elif handle_type == 'Event':
            nevent += 1
        elif handle_type == 'Desktop':
            ndesktop += 1
        elif handle_type == 'Key':
            nkey += 1
        elif handle_type == 'Thread':
            nthread += 1
        elif handle_type == 'Directory':
            ndirectory += 1
        elif handle_type == 'Semaphore':
            nsemaphore += 1
        elif handle_type == 'Timer':
            ntimer += 1
        elif handle_type == 'Section':
            nsection += 1
        elif handle_type == 'Mutant':
            nmutant += 1

avg_handles_per_pid = nhandles / len(pids) if pids else 0

print(f"handles.nhandles: {nhandles}")
print(f"handles.avg_handles_per_pid: {avg_handles_per_pid}")
print(f"handles.nport: {nport}")
print(f"handles.nfile: {nfile}")
print(f"handles.nevent: {nevent}")
print(f"handles.ndesktop: {ndesktop}")
print(f"handles.nkey: {nkey}")
print(f"handles.nthread: {nthread}")
print(f"handles.ndirectory: {ndirectory}")
print(f"handles.nsemaphore: {nsemaphore}")
print(f"handles.ntimer: {ntimer}")
print(f"handles.nsection: {nsection}")
print(f"handles.nmutant: {nmutant}")