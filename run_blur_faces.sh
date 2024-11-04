#!/bin/bash

# Check if input folder is provided
if [ -z "$1" ]; then
  echo "Usage: $0 <input_folder> [output_folder]"
  exit 1
fi

# Set input folder from the first argument
input_folder="$1"

# Check if output folder is provided; if not, create a default
if [ -z "$2" ]; then
  # Create default output folder at the same level as input folder
  parent_dir=$(dirname "$input_folder")
  output_folder="$parent_dir/output_images"
  echo "No output folder provided. Defaulting to: $output_folder"
else
  output_folder="$2"
fi

# Ensure the output folder exists
mkdir -p "$output_folder"

# Run the Python script with specified input and output folders
echo "Running face blurring script..."
python3 main.py "$input_folder" "$output_folder"

echo "Processing complete. Blurred images saved to $output_folder."
