with open('extracted_callbacks.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Initialize counters
total_callbacks = 0
anonymous = 0

for line in lines:
    if "0x" in line:
        total_callbacks += 1
    parts = line.split()
    if len(parts) >= 3 and parts[2] == '-':
        anonymous += 1


print(f"callbacks.total_callbacks: {total_callbacks}")
print(f"callbacks.anonymous: {anonymous}")

