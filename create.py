import os
import re
import glob

def remove_comments(string):
    string = re.sub(re.compile("/\*.*?\*/",re.DOTALL ) ,"" ,string) # remove all occurrences streamed comments (/*COMMENT */) from string
    string = re.sub(re.compile("//.*?\n" ) ,"" ,string) # remove all occurrence single-line comments (//COMMENT\n ) from string
    return string

f1 = open("sample_folder/sample.txt", 'r+')

# Opening all txtFiles
txtFiles = glob.glob('**/*.txt', recursive=True)

file_content = str(f1.read()) 
print(file_content)
file_content = remove_comments(file_content)
print(file_content)

f1.close()

f1 = open("sample_folder/sample.txt", 'w')
f1.write(file_content)

f1.close()



# for txtFile in txtFiles:
#     f = open(txtFile, 'r+')
#     file_content = str(f.read())
#     print("File Content : ", str(file_content))

#     # replacing comments with spaces
#     file_content = remove_comments(file_content)
#     f.write(file_content)

# f.close()

# # Checking for Java Comments
# for txtFile in txtFiles:
#     f = open(txtFile, 'r+')
#     print(f.read())