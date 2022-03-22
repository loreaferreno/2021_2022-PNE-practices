import Seq00

seq1 = "ATTCCCGGGG"

print(f"    Seq:{seq1}")
print(f"    Rev : {Seq00.seq_reverse(seq1)}")
print(f"    Comp: {Seq00.seq_complement(seq1)}")
print(f"    Length: {Seq00.seq_len(seq1)}")
print(f"    A: {Seq00.seq_count_base(seq1, 'A')}")
print(f"    T: {Seq00.seq_count_base(seq1, 'T')}")
print(f"    C: {Seq00.seq_count_base(seq1, 'C')}")
print(f"    G: {Seq00.seq_count_base(seq1, 'G')}")