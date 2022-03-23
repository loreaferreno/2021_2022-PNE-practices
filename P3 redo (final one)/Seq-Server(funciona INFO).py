from colorama import Fore, init
from Seq1 import Seq
import socket
init(autoreset=True)

# -- Step 1: create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Optional: This is for avoiding the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Configure the Server's IP and PORT
PORT = 6123
IP = "127.0.0.1"
seq0 = "AGAGAGAGAGAGAGA"
seq1 = "ATATATATATATATA"
seq2 = "CACACACACACACAC"
seq3 = "TGTGTGTGTGTGTGT"
seq4 = "CGCGCGCGCGCGCGC"
sequences = [seq0, seq1, seq2, seq3, seq4]

# -- Step 1: create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Optional: This is for avoiding the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# -- Step 2: Bind the socket to server's IP and PORT
ls.bind((IP, PORT))

# -- Step 3: Configure the socket for listening
ls.listen()

print("The server is configured!")

while True:
    # -- Waits for a client to connect
    print("Waiting for Clients to connect")

    try:
        (cs, client_ip_port) = ls.accept()

    # -- Server stopped manually
    except KeyboardInterrupt:
        print("Server stopped by the user")

        # -- Close the listenning socket
        ls.close()

        # -- Exit!
        exit()

    # -- Execute this part if there are no errors
    else:

        print("A client has connected to the server!")

        # -- Read the message from the client
        # -- The received message is in raw bytes
        msg_raw = cs.recv(2048)

        # -- We decode it for converting it
        # -- into a human-redeable string
        msg = msg_raw.decode().replace("\n", "").strip()
        splitted_command = msg.split(" ")
        cmd = splitted_command[0]

        if cmd != "PING":
            arg = splitted_command[1]

        if cmd == "PING":
            print(Fore.LIGHTYELLOW_EX + "PING command!!")
            response = "OK!"
            print(f"Message sent to the client: {Fore.BLUE + response}")
            cs.send(response.encode())


        elif cmd == "GET":
            print(Fore.LIGHTYELLOW_EX + "GET command!!")
            exit = False
            while not exit:
                if int(arg) <= 4:
                    response = sequences[int(arg)]
                    cs.send(response.encode())
                    print(sequences[int(arg)])
                    exit = True
                elif int(arg) > 4:
                    response = "The sequences are numbers from 0 to 4"
                    print(response)
                    cs.send(response.encode())
                    exit = True


        elif cmd == "INFO":
            print(Fore.LIGHTYELLOW_EX + "INFO command!!")

            seq = Seq(arg)
            print(f"Sequence: {seq}")
            print("Sequence: " + str(seq))

            print(f"Total length: {seq.len()}")
            print("\nTotal length " + str(seq.len()))

            d = seq.count()

            print("A", seq.seq_count_base("A"), seq.percentages_base(d, "A"), "%")
            response = "A" + " " + str(seq.seq_count_base("A")) + " " + str(seq.percentages_base(d, "A")) + "%" + "\nC" + " " + str(seq.seq_count_base("C"))+ " " + str(seq.percentages_base(d, "C")) + "%" + "\nG"+ " " + str(seq.seq_count_base("G")) +" " + str(seq.percentages_base(d, "G")) + "%" + "\nT" + " " + str(seq.seq_count_base("T"))+ " " + str(seq.percentages_base(d, "T")) + "%"
            cs.send(response.encode())


        elif cmd == "COMP":
            print(Fore.LIGHTYELLOW_EX + "COMP command!!")
            seq = Seq(arg)
            response = seq.complement()
            print(response)
            cs.send(response.encode())

        elif cmd == "REV":
            print(Fore.LIGHTYELLOW_EX + "REV command!!")
            seq = Seq(arg)
            response = seq.reverse()
            print(response)
            cs.send(response.encode())

        elif cmd == "GENE":
            print(Fore.LIGHTYELLOW_EX + "GENE command!!")
            s = Seq()
            folder = "./sequences/"
            s.read_fasta2(folder + arg + ".txt")
            print(s)
            response = str(s)
            cs.send(response.encode())








        # -- Close the data socket
        cs.close()