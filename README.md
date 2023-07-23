# MalDives

Windows Memory Dump Analysis Tool for Malware Detection. Includes Volatility 2.5 for feature extraction.

Static analysis contributed by Andy Wang 
  https://github.com/sinocikid/maldives_new


# How to use:

Clone the repository using:
  ```sh
git clone https://github.com/rykacc/MalDives.git
  ```
Install dependencies:
  ```sh
pip3 install -r requirements.txt
  ```
For dynamic analysis of memory files:
  ```sh
python3 maldives.py -d [path/to/image_file]
  ```
For static analysis of PE files:
  ```sh
python3 maldives.py -s [path/to/image_file]
  ```
