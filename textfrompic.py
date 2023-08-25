import os
import pytesseract
from PIL import Image

# Directory containing your images
image_directory = "/home/phil/Pictures/drinks/jpeg"

# Output directory for text files
output_directory = "/home/phil/pictures/drinks-text"

# Ensure the output directory exists, create it if necessary
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Loop through each image file in the directory
for filename in os.listdir(image_directory):
    if filename.endswith((".jpg", ".png", ".jpeg", ".bmp", ".gif")):
        image_path = os.path.join(image_directory, filename)

        # Open the image using Pillow (PIL)
        img = Image.open(image_path)

        # Use pytesseract to extract text from the image
        # Explicitly specify the language as 'eng' (English)
        extracted_text = pytesseract.image_to_string(img, lang='eng')

        # Create a text file with the same name as the image
        text_filename = os.path.splitext(filename)[0] + ".txt"
        text_filepath = os.path.join(output_directory, text_filename)

        # Write the extracted text to the text file
        with open(text_filepath, "w") as text_file:
            text_file.write(extracted_text)

        print(f"Text extracted from {filename} and saved to {text_filename}")

print("Text extraction complete.")

