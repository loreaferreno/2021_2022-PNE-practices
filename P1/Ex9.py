from Seq1 import Seq
s1 = Seq()
s = s1.get_file()
s2 = s1.read_fasta(s)

print(f"\n  Sequence 1:  (Length: {s2.len()})  {s2}")
d = s2.count()
for k,v in d.items():
    print(k + ":", str(v), end=" ")
print("\nReverse:", s2.reverse())
print("Complementary:", s2.complement())

