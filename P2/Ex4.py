from Client0 import Client
from Seq1 import Seq
import colorama

PRACTICE = 2
EXERCISE = 4

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
IP = "127.0.0.1"
PORT = 6123
# -- Print the IP and PORTs
c = Client(IP, PORT)
print(c)


seq = "FRAT1.txt"
seq1 = "ADA.txt"
seq2 = "FXN.txt"



sequences = [seq, seq1, seq2]
for r in sequences:
    s = Seq()
    s.read_fasta2(r)
    print(f"Sending {colorama.Fore.BLUE + r } to the server..." + colorama.Fore.RESET)
    response = c.talk(f"Sending {r} gene to server" + colorama.Fore.RESET)
    print(f"Response: {colorama.Fore.YELLOW + response + colorama.Fore.RESET}")

    print(f"Sending {colorama.Fore.BLUE + str(s) } to the server..." + colorama.Fore.RESET)
    response = c.talk(s.strbases)
    print(f"Response: {colorama.Fore.YELLOW + response + colorama.Fore.RESET}")


