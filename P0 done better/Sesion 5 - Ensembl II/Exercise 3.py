import Seq00
seqs = ["FRAT1", "ADA", "FXN", "RNU6_269P", "U5"]
for s in seqs:
    folder = "./sequences/"
    sequence = Seq00.seq_read_fasta(s, folder)
    length = Seq00.seq_len(sequence)
    print("DNA file: ", s + ".txt")
    print(length)

