'''
Author: Logan Maupin

This is a collection of functions I use for image processing related stuff.
'''
import os
import requests
from bs4 import BeautifulSoup
import config
import imagehash
from PIL import Image
from io import BytesIO


class Image_Processing:

    @staticmethod
    def difference_image_hashing(filename: str) -> hash:

        # first confirm the file exists
        file_exists = os.path.exists(filename)
        if file_exists:
            try:
                img_hash = imagehash.dhash(Image.open(filename))
                return img_hash
            
            except AttributeError:
                return False
            
    @staticmethod
    def resize_image_to_512x512(img_filename: str) -> None:
        try:
            # Open the image file
            img = Image.open(img_filename)
            
            # Resize the image to 512x512
            img = img.resize((512, 512))
            
            # Save the resized image
            img.save(img_filename)
            print(f"Image '{img_filename}' resized to 512x512 and saved.")
        except Exception as e:
            print(f"An error occurred: {e}")

    @staticmethod
    def get_random_image() -> None:
        # The URL of the website
        url = 'https://thispersondoesnotexist.com/'

        # Send a GET request to the website
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the HTML content with BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find the image tag
            img_tag = soup.find('img')

            if img_tag and 'src' in img_tag.attrs:
                # Get the image URL from the 'src' attribute
                image_url = img_tag['src']

                # Send a GET request to the image URL
                image_response = requests.get(image_url)

                # Check if the image request was successful
                if image_response.status_code == 200:
                    # Open the image and save it
                    image = Image.open(BytesIO(image_response.content))
                    image.save('Profile_Picture.jpg')
                    Image_Processing.resize_image_to_512x512('Profile_Picture.jpg')
