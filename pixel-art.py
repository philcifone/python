import numpy as np
from PIL import Image
from tqdm import tqdm

def pixel_art_generator(image_path, pixel_size, output_path):
    # Open the image
    image = Image.open(image_path)

    # Resize the image to the desired pixel art size
    width, height = image.size
    new_width = width // pixel_size
    new_height = height // pixel_size
    resized_image = image.resize((new_width, new_height), Image.NEAREST)

    # Create a new blank image for the pixel art
    pixel_art = Image.new("RGB", (width, height))

    # Initialize the progress bar
    progress_bar = tqdm(total=new_width * new_height, desc="Generating Pixel Art", unit="pixel")

    # Iterate over each pixel in the resized image
    for x in range(new_width):
        for y in range(new_height):
            # Get the pixel color from the resized image
            pixel_color = resized_image.getpixel((x, y))

            # Scale the pixel color to the original size
            for i in range(pixel_size):
                for j in range(pixel_size):
                    pixel_art.putpixel((x * pixel_size + i, y * pixel_size + j), pixel_color)

            # Update the progress bar
            progress_bar.update()

    # Close the progress bar
    progress_bar.close()

    # Save the pixel art image
    pixel_art.save(output_path)

# Prompt the user for input
image_path = input("Enter the path to the input image file: ")
pixel_size = int(input("Enter the desired pixel size for the pixel art: "))
output_path = input("Enter the output path and filename to save the pixel art image: ")

# Call the pixel art generator function
pixel_art_generator(image_path, pixel_size, output_path)

