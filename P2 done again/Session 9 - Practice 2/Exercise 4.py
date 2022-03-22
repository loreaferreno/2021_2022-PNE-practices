from Client0 import Client
from Seq1 import Seq
from colorama import Fore, init

init(autoreset=True)

PRACTICE = 2
EXERCISE = 4

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
IP = "127.0.0.1"
PORT = 6123

# -- Create a client object
c = Client(IP, PORT)
print(c)

genes = ["ADA.txt", "FRAT1.txt"]
for g in genes:
    s1 = Seq()
    s1.read_fasta(g)

    # -- Send a message to the server

    print("To the server: ", Fore.BLUE + f"Sending {g} gene to the server")
    response = c.talk(Fore.YELLOW + f"Sending {g} gene to server")
    response = c.talk(s1.strbases)
    print(f"Response: {response}")