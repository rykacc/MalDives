with open('extracted_modules.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Initialize counter
total_offsets = 0

for line in lines:
    if line.startswith('0x'):
        total_offsets += 1

print(f"modules.total_offsets: {total_offsets}")
