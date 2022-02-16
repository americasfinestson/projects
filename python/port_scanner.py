#!/usr/bin/env python3

""" Port scans localhost and prints open ports

Arguments: None

Outputs: None

"""

import socket


def main():

    # Get the IPv4 address of localhost
    ip = socket.gethostbyname('localhost')

    for p in range(1,65535):
        # Initiate a socket instance using IPv4 and TCP
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Set default timeout to 0.1s
        socket.setdefaulttimeout(0.1)

        # connect_ex is like connect, but returns an error code instead of exception object
        connection = s.connect_ex((ip, p))
        if connection == 0:
            print("Successfully connected to {}:{}".format(ip, p))
        s.close()
    

if __name__ == '__main__':
    main()

