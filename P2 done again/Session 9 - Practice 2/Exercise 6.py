from Client0 import Client
from Seq1 import Seq
from colorama import Fore, init

init(autoreset=True)

PRACTICE = 2
EXERCISE = 5

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")





s1 = Seq()
filename = Seq.get_file2()
s1.read_fasta(filename)

frag1 = s1.strbases[:10]
frag2 = s1.strbases[11:20]
frag3 = s1.strbases[21:30]
frag4 = s1.strbases[31:40]
frag5 = s1.strbases[41:50]
frag6 = s1.strbases[51:60]
frag7 = s1.strbases[61:70]
frag8 = s1.strbases[71:80]
frag9 = s1.strbases[81:90]
frag10 = s1.strbases[91:100]

fragments_even = [frag2, frag4, frag6, frag8, frag10]
fragments_odd = [frag1, frag3, frag5, frag7, frag9]
i = 2
for f in fragments_even:
    # -- Parameters of the server to talk to
    IP = "127.0.0.1"
    PORT = 6123
    # -- Create a client object
    c = Client(IP, PORT)

    response = c.talk(Fore.YELLOW + f"Sending {i} gene to server")
    i = i + 2

p = 1
for f in fragments_odd:
    # -- Parameters of the server to talk to
    IP = "127.0.0.1"
    PORT = 8080
    # -- Create a client object
    c = Client(IP, PORT)

    response = c.talk(Fore.YELLOW + f"Sending fragment {p} gene to server")
    p = p + 2

s = 1
all_fragments = [frag1, frag2, frag3, frag4, frag5, frag6, frag7, frag8, frag9, frag10]
for t in all_fragments:
    print(f"Fragment {s}: {t}")
    s = s + 1
