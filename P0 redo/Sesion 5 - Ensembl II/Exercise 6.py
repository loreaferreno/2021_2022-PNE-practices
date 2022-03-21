import Seq00
gene, folder = Seq00.get_file()
sequence = Seq00.seq_read_fasta(gene, folder)
print("DNA file: ", gene + ".txt")
print(sequence[:20])
reverse = Seq00.seq_reverse(sequence[:20])
print(reverse)
