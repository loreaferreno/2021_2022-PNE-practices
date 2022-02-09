import seq0

list_genes = ["U5", "FRAT1", "ADA", "FXN", "RNU6_269P"]
for l in list_genes:
    print(len(seq0.seq_read_fasta("./sequences/" + l + ".txt")))


#folder = "./sequences/"
#gene = input("choose a file: ")
#f = open(folder + gene + ".txt")
#print(f.read())
