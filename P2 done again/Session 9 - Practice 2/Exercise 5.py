from Client0 import Client
from Seq1 import Seq
from colorama import Fore, init

init(autoreset=True)

PRACTICE = 2
EXERCISE = 5

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
IP = "127.0.0.1"
PORT = 6123

# -- Create a client object
c = Client(IP, PORT)
print(c)


s1 = Seq()
filename = Seq.get_file2()
s1.read_fasta(filename)

frag1 = s1.strbases[:20]
frag2 = s1.strbases[21:40]
frag3 = s1.strbases[41:60]
frag4 = s1.strbases[61:80]
frag5 = s1.strbases[81:100]

fragments = [frag1, frag2, frag3, frag4, frag5]
i = 0
response = c.talk(Fore.LIGHTYELLOW_EX + "Sending gene FRAT1 to server in fragments of 20 bases")
for f in fragments:
    response = c.talk(Fore.YELLOW + f"Sending {f} gene to server")
    print(f"Fragment{i}: {f}")
    i = i + 1
