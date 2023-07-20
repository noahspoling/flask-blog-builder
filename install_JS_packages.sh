#!/bin/bash

# Create the directory if it doesn't exist
mkdir -p app/static/js/packages

# Read the JSON file and extract the package information
packages=$(jq -r '.packages[] | "\(.path)=\(.cdn_url)"' jsPackages.json)

# Loop through the packages and download them
while IFS='=' read -r path_url; do
    path=$(echo "$path_url" | cut -d '=' -f1)
    url=$(echo "$path_url" | cut -d '=' -f2)
    destination="app/static/js/packages/$path"
    echo "Downloading $path..."
    curl -sSL "$url" -o "$destination"
    echo "$path downloaded."
done <<< "$packages"

echo "Packages installation completed."
