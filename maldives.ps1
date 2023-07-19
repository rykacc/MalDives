param (
    [Parameter(Mandatory=$true)]
    [string]$f
)

Write-Host "Activating Python 2.7 environment (py27)..."
conda activate py27

Write-Host "Running extract.py script with Python 2.7..."
python extract.py $f

Write-Host "Deactivating Python 2.7 environment..."
conda deactivate

Write-Host "Activating Python 3 environment (base)..."
conda activate base

Write-Host "Running maldives.py script with Python 3..."
python maldives.py

Write-Host "Deactivating Python 3 environment..."
conda deactivate

Write-Host "Done."
