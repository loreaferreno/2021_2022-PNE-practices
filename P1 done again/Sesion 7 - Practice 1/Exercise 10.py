from Seq1 import Seq
# -- Create a Null sequence
s = Seq()
filename = Seq.get_file2()
# -- Initialize the null seq with the given file in fasta format
s.read_fasta(filename)

print(f"Sequence 1: (Length:{s.len()}) {filename}")
print(f"Bases: {s.count()}")
print(f"Reverse: {s.reverse()}")
print(f"Complementary: {s.complement()}")
d = s.count()
print(f"Gene {filename} : \nMost frequent value base: {s.processing_genes(d)}")