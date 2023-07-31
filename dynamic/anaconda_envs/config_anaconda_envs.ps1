# Update conda to the latest version
conda update -n base -c defaults conda

# Create the base environment
conda env create -f base_environment.yml

# Create the Python 2.7 environment
conda env create -f py27_environment.yml
