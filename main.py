import sys
import os
from face_blurring import process_images  # Ensure process_images function is imported from face_blurring.py

def main():
    # Check if input and output paths are provided as command-line arguments
    if len(sys.argv) < 2:
        print("Usage: python main.py <input_folder> [output_folder]")
        sys.exit(1)

    # Get input folder from the first argument
    input_folder = sys.argv[1]

    # Check if an output folder is provided; if not, create a default
    if len(sys.argv) > 2:
        output_folder = sys.argv[2]
    else:
        # Create default output folder at the same level as input folder
        parent_dir = os.path.dirname(input_folder)
        output_folder = os.path.join(parent_dir, "output_images")
        print(f"No output folder provided. Defaulting to: {output_folder}")

    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Run the face blurring process
    process_images(input_folder, output_folder)
    print(f"Processing complete. Blurred images saved to {output_folder}")

if __name__ == "__main__":
    main()
