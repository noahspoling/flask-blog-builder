# Create the directory if it doesn't exist
New-Item -ItemType Directory -Force -Path "app/static/js/packages"

# Read the JSON file and extract the package information
$json = Get-Content -Raw -Path "jsPackages.json" | ConvertFrom-Json
$packages = $json.packages

# Loop through the packages and download them
foreach ($package in $packages) {
    $path = $package.path
    $cdnUrl = $package.cdn_url
    $destination = Join-Path -Path "app/static/js/packages" -ChildPath $path

    Write-Host "Downloading $path..."
    Invoke-WebRequest -Uri $cdnUrl -OutFile $destination
    Write-Host "$path downloaded."
}

Write-Host "Packages installation completed."
