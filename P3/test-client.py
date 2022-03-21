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
    option = input("What command do you want to test? ")
    if option.lower() == "ping":
        print("*Testing PING...")
        response = c.talk("PING")
        print(response)
    elif option.lower() == "get":
        print("*Testing GET...")
        exit = False
        while not exit:
            option2 = input("Which sequence do you want to get? (or exit)")
            if option2.lower() == "exit":
                exit = True
            else:
                response = c.talk(f"GET {option2}")
                print(response)
    elif option.startswith("INFO"):
        print("Testing INFO command...")
        response = c.talk(option)
        print(response)
    elif option.startswith("COMP"):
        print("Testing que COMP command...")
        response = c.talk(option)
        print(response)
    elif option.startswith("REV"):
        print("Testing the REV command...")
        response = c.talk(option)
        print(response)
    elif option.lower() == "gene":
        print("*Testing GENE...")
        exit = False
        while not exit:
            option2 = input("Which gene do you want to get? (or exit)")
            if option2.lower() == "exit":
                exit = True
            else:
                response = c.talk(f"GENE {option2}")
                print(response)
    elif option.lower == "exit":
        exit = True


