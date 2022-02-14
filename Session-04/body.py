from pathlib import Path

# -- Constant with the new of the file to open
FILENAME = "U5.txt"

# -- Open and read the file
file_contents = Path(FILENAME).read_text()

info_dna_2 = file_contents[file_contents.find("\n"):]
print(info_dna_2)