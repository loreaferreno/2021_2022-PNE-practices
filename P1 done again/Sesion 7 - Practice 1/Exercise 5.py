from Seq1 import Seq
# -- Create a Null sequence
s1 = Seq()

# -- Create a valid sequence
s2 = Seq("ACTGA")

# -- Create an invalid sequence
s3 = Seq("Invalid sequence")

print(f"Sequence 1: (Length:{s1.len()}) {s1}")
print("A:", s1.seq_count_base("A"), "C:", s1.seq_count_base("C"), "G:", s1.seq_count_base("G"), "T:", s1.seq_count_base("T"))
print(f"Sequence 2: (Length:{s2.len()}) {s2}")
print("A:", s2.seq_count_base("A"), "C:", s2.seq_count_base("C"), "G:", s2.seq_count_base("G"), "T:", s2.seq_count_base("T"))
print(f"Sequence 3: (Length:{s3.len()}) {s3}")
print("A:", s3.seq_count_base("A"), "C:", s3.seq_count_base("C"), "G:", s3.seq_count_base("G"), "T:", s3.seq_count_base("T"))