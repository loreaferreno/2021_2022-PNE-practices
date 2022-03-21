from pathlib import Path
filename = input("Please enter the name of the file: ")
file_content = Path(filename).read_text()
first_line = file_content[:file_content.find("\n")]
print(first_line)

