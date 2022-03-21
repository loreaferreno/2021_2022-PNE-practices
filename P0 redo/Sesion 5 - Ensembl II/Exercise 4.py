import Seq00
seqs = ["FRAT1", "ADA", "FXN", "RNU6_269P", "U5"]
for s in seqs:
    folder = "./sequences/"
    sequence = Seq00.seq_read_fasta(s, folder)
    count_a, count_c, count_g, count_t = Seq00.seq_count_base(sequence)
    print("DNA file: ", s + ".txt")
    print("A:", count_a, "C:", count_c, "G:", count_g, "t:", count_t,)
