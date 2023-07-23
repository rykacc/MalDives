#!/bin/bash
echo "Starting MalDives Dynamic Analysis..."

# Check if memory dump file was passed as argument
if [ $# -eq 0 ]; then
    echo "No arguments provided. Please provide the memory dump file as an argument."
    exit 1
fi

# Path to your .dmp file
memory_file=$1

# Get the file type using the file command
file_type=$(file --brief --mime-type "$memory_file")

# Check if the file is of the correct type
if [ "$file_type" != "application/octet-stream" ] && [ "$file_type" != "application/x-msdownload" ]; then
    echo "Invalid file type. Only Windows memory dump files supported by Volatility 2.5 are accepted."
    exit 1
fi

# Volatility2.5 path
vol_path="./volatility-master/vol.py"

# Profile
profile="Win7SP1x86"

# Array of plugin names to run
plugins=("pslist" "dlllist" "handles" "ldrmodules" "malfind" "psxview" "modules" "svcscan" "callbacks")

# Run each plugin and append its output to a separate text file
for plugin in "${plugins[@]}"
do
    echo "Extracting $plugin..."
    python2 $vol_path -f $memory_file --profile $profile $plugin > "extracted_${plugin}.txt"
done

echo "Completed. Please check the output text files for each plugin."

# Run the python script
echo "Running maldives.py..."
python3 ./maldives.py $memory_file

