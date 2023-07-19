with open('extracted_psxview.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Initialize counters
not_in_pslist = 0
not_in_psscan = 0
not_in_thrdproc = 0
not_in_pspcid = 0
not_in_csrss = 0
not_in_session = 0
not_in_deskthrd = 0
total_offsets = 0

# Start processing from the second line to skip the header
for line in lines[1:]:
    parts = line.split()
    # We can count the offset as soon as we know the line isn't empty
    if len(parts) > 0:
        total_offsets += 1
    # Ensure there are enough parts to avoid IndexError
    if len(parts) >= 10:
        if parts[3] == 'False':
            not_in_pslist += 1
        if parts[4] == 'False':
            not_in_psscan += 1
        if parts[5] == 'False':
            not_in_thrdproc += 1
        if parts[6] == 'False':
            not_in_pspcid += 1
        if parts[7] == 'False':
            not_in_csrss += 1
        if parts[8] == 'False':
            not_in_session += 1
        if parts[9] == 'False':
            not_in_deskthrd += 1

# Calculate averages
not_in_pslist_avg = not_in_pslist / total_offsets if total_offsets != 0 else 0
not_in_psscan_avg = not_in_psscan / total_offsets if total_offsets != 0 else 0
not_in_thrdproc_avg = not_in_thrdproc / total_offsets if total_offsets != 0 else 0
not_in_pspcid_avg = not_in_pspcid / total_offsets if total_offsets != 0 else 0
not_in_csrss_avg = not_in_csrss / total_offsets if total_offsets != 0 else 0
not_in_session_avg = not_in_session / total_offsets if total_offsets != 0 else 0
not_in_deskthrd_avg = not_in_deskthrd / total_offsets if total_offsets != 0 else 0

# Print results
print(f"psxview.not_in_pslist: {not_in_pslist}")
print(f"psxview.not_in_psscan: {not_in_psscan}")
print(f"psxview.not_in_thrdproc: {not_in_thrdproc}")
print(f"psxview.not_in_pspcid: {not_in_pspcid}")
print(f"psxview.not_in_csrss: {not_in_csrss}")
print(f"psxview.not_in_session: {not_in_session}")
print(f"psxview.not_in_deskthrd: {not_in_deskthrd}")
print(f"psxview.not_in_pslist_avg: {not_in_pslist_avg}")
print(f"psxview.not_in_psscan_avg: {not_in_psscan_avg}")
print(f"psxview.not_in_thrdproc_avg: {not_in_thrdproc_avg}")
print(f"psxview.not_in_pspcid_avg: {not_in_pspcid_avg}")
print(f"psxview.not_in_csrss_avg: {not_in_csrss_avg}")
print(f"psxview.not_in_session_avg: {not_in_session_avg}")
print(f"psxview.not_in_deskthrd_avg: {not_in_deskthrd_avg}")
