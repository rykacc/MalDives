import re

with open('extracted_ldrmodules.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Initialize counters
not_in_load = 0
not_in_init = 0
not_in_mem = 0
total_modules = 0

for line in lines:
    parts = line.split()
    if len(parts) < 6:
        continue
    total_modules += 1
    if parts[3] == 'False':
        not_in_load += 1
    if parts[4] == 'False':
        not_in_init += 1
    if parts[5] == 'False':
        not_in_mem += 1

not_in_load_avg = not_in_load / total_modules if total_modules != 0 else 0
not_in_init_avg = not_in_init / total_modules if total_modules != 0 else 0
not_in_mem_avg = not_in_mem / total_modules if total_modules != 0 else 0

print(f"ldrmodules.not_in_load: {not_in_load}")
print(f"ldrmodules.not_in_init: {not_in_init}")
print(f"ldrmodules.not_in_mem: {not_in_mem}")
print(f"ldrmodules.not_in_load_avg: {not_in_load_avg}")
print(f"ldrmodules.not_in_init_avg: {not_in_init_avg}")
print(f"ldrmodules.not_in_mem_avg: {not_in_mem_avg}")
