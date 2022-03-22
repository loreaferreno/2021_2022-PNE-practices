from Seq01 import Seq
seq_list = [Seq("ACT"), Seq("GATA"), Seq("CAGATA")]
indice = 0
for seq in seq_list:
    seq.print_seqs(indice)
    indice += 1

