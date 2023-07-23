import sys
import subprocess
import os
import struct

def is_pe_file(file):
    try:
        with open(file, 'rb') as f:
            # Read the first two bytes and check if they're 'MZ'
            if f.read(2) != b'MZ':
                return False

            # Go to the offset specified in the e_lfanew field (usually 0x3C)
            f.seek(0x3C, os.SEEK_SET)
            pe_offset = struct.unpack('<I', f.read(4))[0]

            # Go to the beginning of the PE header
            f.seek(pe_offset, os.SEEK_SET)

            # Read the PE magic number ('PE\0\0')
            return f.read(4) == b'PE\0\0'
    except Exception as e:
        print(f"Error reading file: {str(e)}")
        return False

def run_PE(file):
    # Execute the PE scanner with the given file
    subprocess.run(["python3", "Extract/PE_main.py", file])

if __name__ == "__main__":
    # Expecting file path as a command line argument
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <file_path>")
        sys.exit(1)

    file = sys.argv[1]

    if not is_pe_file(file):
        print("Invalid file type. Only PE files are accepted.")
        sys.exit(1)

    print("Analyzing static file...")
    
    # Run PE scanner
    run_PE(file)

