#!/usr/bin/env python3

import os
import sys
import socket


def main():

    # Define machine to port scan
    machine = socket.gethostbyname('localhost')

    for p in range(1,65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)

        connection = s.connect_ex((machine, p))
        if connection == 0:
            print("Successfully connected to {}:{}".format(machine, p))
        s.close()
    

if __name__ == '__main__':
    main()

