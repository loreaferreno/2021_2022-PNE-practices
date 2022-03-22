from Seq1 import Seq

s1 = Seq()
filename = Seq.get_file2()
s1.read_fasta2(filename)

print(f"\n  Sequence 1:  (Length: {s1.len()})  {s1}")
d = s1.count()
for k,v in d.items():
    print(k + ":", str(v), end=" ")
print("\nReverse:", s1.reverse())
print("Complementary:", s1.complement())

