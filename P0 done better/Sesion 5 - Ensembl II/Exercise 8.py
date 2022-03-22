import Seq00
seqs = ["FRAT1", "ADA", "FXN", "RNU6_269P", "U5"]
folder = "./sequences/"
for s in seqs:
    sequence = Seq00.seq_read_fasta(s, folder)
    print("DNA file: ", s + ".txt")
    d = Seq00.seq_count(sequence)
    base = Seq00.processing_genes(d)
    print(base)