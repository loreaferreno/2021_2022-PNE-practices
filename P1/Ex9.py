import self as self

import P1.Seq1
from Seq1 import Seq
filename = Seq.get_file(self)
s1 = Seq()
s2 = s1.read_fasta(filename)
print(s2)

print(f"\n  Sequence 2: {s2} (Length: {s2.len()})  ")
d = s2.count()
for k,v in d.items():
    print(k + ":", str(v), end=" ")
print("\nReverse:", s2.reverse())
print("Complementary:", s2.complement())

