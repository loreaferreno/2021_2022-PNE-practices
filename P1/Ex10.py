from Seq1 import Seq


def get_file():
    exit = False
    while not exit:
        folder = "./sequences/"
        filename = input("Enter the name of the file: ")
        try:
            print(folder + filename + ".txt")
            f = open(folder + filename + ".txt", "r")
            exit = True
            return folder + filename + ".txt"
        except FileNotFoundError:
            if self.filename.lower() == "exit":
                print("The program is finished. You pressed exit.")
                filename = "none"
                exit = True
                return filename
            else:
                print("File was not found")


s1 = Seq()
filename = get_file()
s1.read_fasta2(filename)

print(f"\n  Sequence 1:  (Length: {s1.len()})  {s1}")
d = s1.count()
for k,v in d.items():
    print(k + ":", str(v), end=" ")
print("\nReverse:", s1.reverse())
print("Complementary:", s1.complement())
base = s1.processing_genes(d)
print(f"Gene {filename} : \nMost frequent value base: {base}")