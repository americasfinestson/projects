#!/usr/bin/env/python3

""" Creates a botnet from specified hosts (in this case, just loopback)

Arguments: None

"""

import pxssh
import os

class Client:

    def __init__(self, hostname, username, password)
        self.hostname = hostname
        self.username = username
        self.password = password
        self.session = self.connect()

    def connect(self):
        try:
            session = pxssh.pxssh()
            session.login(self.hostname, self.username, self.password)
            return session
        except Exception as e:
            print(e)
            print('Error connecting to host')

    def send_command(self, command):
        self.session.sendline(cmd)
        self.session.prompt()
        return self.session.before

def send_command_to_bot(command)

    for client in botnet:
        output = client.send_command(command)
        print("[*] Current host: " + client.hostname)
        print("[*] " + output)


def main():

    client = Client(hostname, username, password)
    botnet.append(client)


if __name__ == '__main__':

    main()
