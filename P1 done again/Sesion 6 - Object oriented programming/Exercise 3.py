from Seq01 import Seq

seq_list1 = Seq.generate_seqs("A", 3)
seq_list2 = Seq.generate_seqs("AC", 5)

print(seq_list1)
print(seq_list2)

print("List 1:")
Seq.print_seqs(seq_list1, 3)

print()
print("List 2:")
Seq.print_seqs(seq_list2, 5)