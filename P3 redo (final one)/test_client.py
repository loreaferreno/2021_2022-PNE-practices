from client0 import Client
from colorama import Fore, init
init(autoreset=True)


PRACTICE = 3
EXERCISE = 7

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
IP = "127.0.0.1"
PORT = 6123
# -- Print the IP and PORTs
c = Client(IP, PORT)
print(c)

exit = False
while not exit:
    msg = input("What command do you want to test?: ")
    print(Fore.LIGHTCYAN_EX + f"*Testing {msg} command..")
    c.talk(msg)
    response = c.talk(msg)
    print(response)

