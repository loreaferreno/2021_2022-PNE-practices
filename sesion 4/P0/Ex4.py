import seq0
filename = seq0.get_file()
full_seq = seq0.seq_read_fasta(filename)
folder = "./sequences/"
gene = input("choose a file: ")
f = open(folder + gene + ".txt")
d = seq0.count_bases(full_seq)
print(d)