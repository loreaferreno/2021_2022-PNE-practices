from Client0 import Client
from Seq1 import Seq


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
    option = input("What do you want to test? ")
    if option.lower() == "ping":
        print("*Testing PING...")
        response = c.talk("PING")
        print(response)
    elif option.startswith("GET"):
        print("*Testing GET...")
        response = c.talk(option)
        print(response)
    elif option.lower == "exit":
        exit = True


