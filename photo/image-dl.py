import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# URL of the webpage with the images
url = "https://philcifone.com/photos/night/"

# Send an HTTP GET request to the URL
response = requests.get(url)

if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")

    # Create a directory to save the images
    download_dir = "night_images"
    os.makedirs(download_dir, exist_ok=True)

    # Find all image elements in the HTML
    img_tags = soup.find_all("img")

    # Download and save each image
    for img_tag in img_tags:
        img_url = img_tag.get("src")
        if img_url:
            img_url = urljoin(url, img_url)
            img_name = img_url.split("/")[-1]
            img_path = os.path.join(download_dir, img_name)

            response = requests.get(img_url)
            if response.status_code == 200:
                with open(img_path, "wb") as img_file:
                    img_file.write(response.content)
                print(f"Downloaded: {img_name}")
            else:
                print(f"Failed to download: {img_url}")

    print("Images downloaded successfully.")
else:
    print("Failed to retrieve the webpage.")
