import seq0
filename = seq0.get_file()
sequence = seq0.seq_read_fasta(filename)
print(sequence[:20])
