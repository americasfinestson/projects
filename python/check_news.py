#!/usr/bin/env python3

""" WORK IN PROGRESS - Creates a list of headlines from the provided news source.

Usage:

    python3 check_news.py --url=https://web.site

Arguments:

    --url
        Description: The URL of the news website to pull headlines from
        Type: str
        Required: True
        Example: --url=cnn.com
"""

import argparse
import requests
import requests_html
import sys
from pprint import pprint


def read_user_input():

    parser = argparse.ArgumentParser()
    parser.add_argument('--url')
    args = parser.parse_args()

    if not args.url:
        sys.exit('ERROR: This script must be called with one argument. Please see the docstring for more information..\n')

    return args.url


def pull_content(url):

    try:
        r = requests.get(url)
    except requests.exceptions.ConnectionError as e:
        sys.exit('Uh oh, it appears the website ' + url + ' is not available at this time!')
    if r.ok:
        return r


def main():

    url = read_user_input()
    r = pull_content(url)
    pprint(r.text)


if __name__ == '__main__':

    main()

