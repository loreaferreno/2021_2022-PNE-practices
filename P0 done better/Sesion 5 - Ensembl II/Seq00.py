from pathlib import Path
def seq_ping():
    print("OK")


def get_file():
    exit = False
    while not exit:
        folder = "./sequences/"
        folder2 = folder
        gene = input("Enter the name of the file: ")
        gene2 = gene
        try:
            filename = open(folder2 + gene2 + ".txt", "r")
            exit = True
            return gene, folder
        except FileNotFoundError:
            if gene.lower() == "exit":
                print("The program is finished. You pressed exit.")
                filename = "none"
                exit = True
                return filename, gene
            else:
                print("File was not found")


def seq_read_fasta(gene, folder):
    file = folder + gene + ".txt"
    full_seq = Path(file).read_text()
    full_seq = full_seq[full_seq.find("\n"):].replace("\n", "")
    return full_seq


def seq_len(s):
    return len(s)


def seq_count_base(full_seq, base):
    count_a = 0
    count_c = 0
    count_g = 0
    count_t = 0
    for i in full_seq:
        if i == "A":
            count_a += 1
        elif i == "C":
            count_c += 1
        elif i == "G":
            count_g += 1
        elif i == "T":
            count_t += 1
    if base == "A":
        return count_a
    elif base == "C":
        return count_c
    elif base == "G":
        return count_g
    elif base == "T":
        return count_t


def seq_count_base2(full_seq):
    count_a = 0
    count_c = 0
    count_g = 0
    count_t = 0
    for i in full_seq:
        if i == "A":
            count_a += 1
        elif i == "C":
            count_c += 1
        elif i == "G":
            count_g += 1
        elif i == "T":
            count_t += 1
    return count_a, count_c, count_g, count_t


def seq_count(full_seq):
    d = {"A": 0, "C": 0, "G": 0, "T": 0}
    for b in full_seq:
        d[b] += 1
    return d


def seq_reverse(sequence):
    reverse = sequence[::-1]
    return reverse


def seq_complement(sequence):
    complementary = ""
    for i in sequence:
        if i == "A":
            complementary += "T"
        elif i == "T":
            complementary += "A"
        elif i == "C":
            complementary += "G"
        elif i == "G":
            complementary += "C"
    return complementary


def processing_genes(d):
    highest_value = 0
    for k, v in d.items():
        if int(v) > highest_value:
            highest_value = int(v)
            base = k
    return base

