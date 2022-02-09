def seq_ping():
    print("ok")


def get_file():
    exit = False
    while not exit:
        filename = input("Enter the name of the file: ")
        try:
            f = open(filename, "r")
            exit = True
            return filename
        except FileNotFoundError:
            print("File was not found")


def seq_read_fasta(filename):
            full_seq = open(filename, "r").read()
            full_seq = full_seq[full_seq.find("\n"):].replace("\n", "")
            return full_seq

def count_bases(full_seq):
    d = {"A": 0, "C": 0, "G": 0, "T": 0}
    for b in full_seq:
        d[b] += 1
    return d
