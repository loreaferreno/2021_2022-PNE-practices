from pathlib import Path
filename = input("Please enter the name of the file: ")
file_content = Path(filename).read_text()
file_body = file_content[file_content.find("\n"):]
body_without_eof = file_body.replace("\n", "")
print(len(body_without_eof))

