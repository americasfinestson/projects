#!/usr/bin/env python3

""" Create an RPM from a user-specified name out of the contents (recursive) of the directory the script is called from.

Usage:

    python3 create_rpm.py --rpm_name=<desired name>

Arguments:

    --rpm_name
        Description: The name of the RPM this script will create
        Type: str
        Required: True
        Example: --rpm_name=mypkg
"""

import os
import sys
import argparse
from pprint import pprint as pp

def read_user_input():

    parser = argparse.ArgumentParser()
    parser.add_argument('--rpm_name')
    args = parser.parse_args()

    if not args.rpm_name:
    
        sys.exit("ERROR: This script must be called with one argument. Please see the docstring for more information..\n")

    return args.rpm_name

def main():

    # Read and validate user input
    rpm_name = read_user_input()

    # Create rpmbuild directories
    cwd = os.getcwd()
    rpmdirs = [ '/BUILD',
                '/BUILDROOT',
                '/RPMS',
                '/SOURCES',
                '/SPECS',
                '/SRPMS' ]
    full_path_rpm_dirs = [cwd + p for p in rpmdirs]


if __name__ == '__main__':

    main()

