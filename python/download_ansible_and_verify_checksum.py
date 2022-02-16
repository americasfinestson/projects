#!/usr/bin/env python3

import requests_html
import hashlib
import os


def download_file(*args):

    ansible = requests_html.HTMLSession().get(args[0]) 

    with open(args[1], 'wb') as f:
        f.write(ansible.content)
        f.close()


def get_vendor_sha256(*args):

    ansible_hash_content = requests_html.HTMLSession().get(args[0])
    ansible_hash_table = ansible_hash_content.html.find('table.table.table--hashes', first=True)
    ansible_hash_table_body = ansible_hash_content.html.find('tbody', first=True)
    return ansible_hash_table_body.text.split('\n')[1]


def get_downloaded_sha256(*args):

    with open(args[0], 'rb') as f:
        data = f.read()
        f.close()

    return hashlib.sha256(data).hexdigest()


def main():

    download_link = 'https://files.pythonhosted.org/packages/d3/67/ceac5a18e6b675e7ea5330a0737625593ab8f9706c1ed31071c29b62322c/ansible-5.3.0.tar.gz'
    download_path = 'ansible.tar.gz'
    hash_link = 'https://pypi.org/project/ansible/#copy-hash-modal-b9172500-c8ab-40c9-b5a8-87987dbb7bf7'

    # Download Ansible and save it locally
    download_file(download_link, download_path)
    print("Successfully downloaded Ansible...")
    print()

    # Get vendor-provided SHA256 
    vendor_sha256_hash = get_vendor_sha256(hash_link) 
    print("The vendor-provided SHA256 hash for the Ansible download is:")
    print("\t\t{}".format(vendor_sha256_hash))
    print()

    # Get downloaded SHA256
    downloaded_sha256_hash = get_downloaded_sha256(download_path)
    print("The SHA256 hash for the downloaded version of Ansible is:")
    print("\t\t{}".format(downloaded_sha256_hash))
    print()

    if downloaded_sha256_hash == vendor_sha256_hash:
        print("Success! Hashes match!")
    else:
        print("It appears the download may have been corrupted. Please try again!")

    os.remove(download_path)


if __name__ == '__main__':

    main()
