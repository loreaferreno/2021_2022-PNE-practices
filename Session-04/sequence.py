from pathlib import Path

# -- Constant with the new of the file to open
FILENAME = "ADA.txt"

# -- Open and read the file
file_contents = Path(FILENAME).read_text()

info_dna = file_contents[file_contents.find("\n"):].replace("\n", "")
count = 0
for i in info_dna:
    count += 1
print(count)
