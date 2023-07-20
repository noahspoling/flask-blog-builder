# Check if directory exists
if (-not (Test-Path -Path ".venv" -PathType Container)) {
    Write-Host "Creating python virtual environment..."
    python -m venv .venv
}

Write-Host "Activating virtual environment..."
. .venv/Scripts/Activate.ps1

Write-Host "Installing dependencies..."
pip install -r pythonRequirements.txt
