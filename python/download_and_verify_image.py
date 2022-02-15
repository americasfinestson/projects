#!/usr/bin/env python3

import requests_html
import hashlib
from PIL import Image
from cryptography.fernet import Fernet


def download_image(*args):

    img = requests_html.HTMLSession().get(args[0]) 

    with open(args[1], 'wb') as f:

        f.write(img.content)
        f.close()
    
def main():

    url = 'https://content-blockchain.org/wp-content/uploads/2018/02/cats-1024x768.jpg'
    image_path = 'image.png'

    # Download image and save it locally
    download_image(url, image_path)
    # Hash the image
    image_hash = hashlib.sha512(Image.open(image_path).tobytes()).hexdigest()
    # Encryption
    # Generate key
    key = Fernet.generate_key()
    # Initiate a Fernet class instance
    fernet = Fernet(key)
    # Encrypt the image hash
    image_hash_enc = fernet.encrypt(image_hash.encode())
    # Decrypt the hash
    image_hash_dec = fernet.decrypt(image_hash_enc)

    print(image_hash)
    print(image_hash_enc.decode())
    print(image_hash_dec.decode())



if __name__ == '__main__':

    main()
