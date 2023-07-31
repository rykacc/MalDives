import argparse
import subprocess
from pyfiglet import Figlet

# create a Figlet object
f = Figlet(font='smslant')

# print a banner when the script starts
print(f.renderText('MalDives'))

# create the top-level parser
parser = argparse.ArgumentParser(prog='maldives.py', description='Perform either static or dynamic analysis with the given file or memory dump.')

# add the arguments
parser.add_argument('-d', metavar='dynamic', type=str, help='Perform dynamic analysis on the given image file.')
parser.add_argument('-s', metavar='static', type=str, help='Perform static analysis on the given file.')
parser.add_argument('-c', metavar='csv', type=str, help='Perform csv analysis on the given file.')

args = parser.parse_args()

# Check if no arguments were provided, if true print help message
if not any(vars(args).values()):
    parser.print_help()
else:
    if args.d:
        # Execute dynamic analysis (maldives.sh script)
        subprocess.run(["./maldives.sh", args.d], cwd="./dynamic")
    elif args.s:
        # Execute static analysis (main.py script)
        subprocess.run(["python3", "main.py", args.s], cwd="./static")
    elif args.c:
        # Execute CSV analysis (directcsv.py script)
        subprocess.run(["python3", "directcsv.py", args.c], cwd="./dynamic")

