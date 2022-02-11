import seq0
exit = False
while not exit:
    filename, gene = seq0.get_file()
    if filename == "none":
        exit = True
    else:
        full_seq = seq0.seq_read_fasta(filename)
        d = seq0.seq_count(full_seq)
        base = seq0.processing_genes(d)
        print(base)