from Client0 import Client

PRACTICE = 2
EXERCISE = 2

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
IP = "10.3.34.224"
PORT = 8080
# -- Print the IP and PORTs
c = Client(IP, PORT)
print(c)