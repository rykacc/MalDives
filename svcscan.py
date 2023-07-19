with open('extracted_svcscan.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Initialize counters
nservices = 0
kernel_drivers = 0
fs_drivers = 0
process_services = 0
shared_process_services = 0
interactive_process_services = 0
nactive = 0

for line in lines:
    if "Offset:" in line:
        nservices += 1
    elif "SERVICE_KERNEL_DRIVER" in line:
        kernel_drivers += 1
    elif "SERVICE_FILE_SYSTEM_DRIVER" in line:
        fs_drivers += 1
    elif "SERVICE_WIN32_OWN_PROCESS" in line:
        process_services += 1
    elif "SERVICE_WIN32_SHARE_PROCESS" in line:
        shared_process_services += 1
    elif "SERVICE_INTERACTIVE_PROCESS" in line:
        interactive_process_services += 1
    elif "SERVICE_RUNNING" in line:
        nactive += 1

print(f"svcscan.nservices: {nservices}")
print(f"svcscan.kernel_drivers: {kernel_drivers}")
print(f"svcscan.fs_drivers: {fs_drivers}")
print(f"svcscan.process_services: {process_services}")
print(f"svcscan.shared_process_services: {shared_process_services}")
print(f"svcscan.interactive_process_services: {interactive_process_services}")
print(f"svcscan.nactive: {nactive}")
