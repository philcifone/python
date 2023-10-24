import os
import subprocess

# Directory containing your HEIC images
heic_directory = "/home/phil/Pictures/drinks"

# Output directory for JPEG images
jpeg_directory = "/home/phil/Pictures/drinks/jpeg"

# Ensure the output directory exists, create it if necessary
if not os.path.exists(jpeg_directory):
    os.makedirs(jpeg_directory)

# Loop through each HEIC image file in the directory
for filename in os.listdir(heic_directory):
    if filename.lower().endswith(".heic"):
        heic_path = os.path.join(heic_directory, filename)

        # Create the output JPEG filename
        jpeg_filename = os.path.splitext(filename)[0] + ".jpg"
        jpeg_path = os.path.join(jpeg_directory, jpeg_filename)

        # Use "heif-convert" to convert HEIC to JPEG
        command = f"heif-convert '{heic_path}' '{jpeg_path}'"
        subprocess.run(command, shell=True, check=True)

        print(f"Converted {filename} to {jpeg_filename}")

print("HEIC to JPEG conversion complete.")

