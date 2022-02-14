import seq0
exit = False
while not exit:
    filename, gene = seq0.get_file()
    if filename == "none":
        exit = True
    else:
        full_seq = seq0.seq_read_fasta(filename)
        complementary = seq0.seq_complement(full_seq)
        print(complementary)