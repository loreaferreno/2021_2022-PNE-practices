import Seq00
seqs = ["FRAT1", "ADA", "FXN", "RNU6_269P", "U5"]
for s in seqs:
    folder = "./sequences/"
    sequence = Seq00.seq_read_fasta(s, folder)
    count_a = Seq00.seq_count_base(sequence, "A")
    print("DNA file: ", s + ".txt")
    print(count_a)
