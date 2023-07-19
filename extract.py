import os
import sys
import subprocess

# Check if memory dump file was passed as argument
if len(sys.argv) < 2:
    print("No arguments provided. Please provide the memory dump file as an argument.")
    sys.exit(1)

# Path to your .dmp file
memory_file = sys.argv[1]

# Volatility2.5 path
vol_path = os.path.join(os.getcwd(), "volatility-master", "vol.py")

# Path to your Python 2.7 interpreter in Anaconda - replace with your own if different
python2_path = os.path.join(sys.prefix, "python.exe")  # This uses the Python executable from the active Anaconda environment

# Profile
profile = "Win7SP1x86"

# Array of plugin names to run
plugins = ["pslist", "dlllist", "handles", "ldrmodules", "malfind", "psxview", "modules", "svcscan", "callbacks"]

# Run each plugin and append its output to a separate text file
for plugin in plugins:
    print("Extracting {}...".format(plugin))
    output_file = "extracted_{}.txt".format(plugin)
    command = [python2_path, vol_path, "-f", memory_file, "--profile", profile, plugin]

    with open(output_file, 'w') as f:
        process = subprocess.Popen(command, stdout=f)
        process.communicate()

print("Completed. Please check the output text files for each plugin.")
