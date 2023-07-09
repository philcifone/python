from PIL import Image
import sys

def merge_images(image1_path, image2_path, output_path):
    image1 = Image.open(image1_path)
    image2 = Image.open(image2_path)

    # Ensure that both images have the same dimensions
    if image1.size != image2.size:
        raise ValueError("The images must have the same dimensions.")

    # Create a new image with the same size as the input images
    merged_image = Image.new("RGB", image1.size)

    # Get the pixel data for both input images
    pixels1 = image1.load()
    pixels2 = image2.load()

    # Iterate over each pixel in the image
    for x in range(image1.width):
        for y in range(image1.height):
            # Merge every other pixel from image1 and image2
            if (x + y) % 2 == 0:
                merged_pixel = pixels1[x, y]
            else:
                merged_pixel = pixels2[x, y]

            # Set the merged pixel in the new image
            merged_image.putpixel((x, y), merged_pixel)

    # Save the merged image
    merged_image.save(output_path)
    print("Merged image saved successfully.")

if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 4:
        print("Usage: python merge_images.py <image1_path> <image2_path> <output_path>")
    else:
        # Retrieve the arguments
        image1_path = sys.argv[1]
        image2_path = sys.argv[2]
        output_path = sys.argv[3]

        # Call the function to merge the images
        merge_images(image1_path, image2_path, output_path)
