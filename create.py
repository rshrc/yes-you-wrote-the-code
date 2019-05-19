import os
import re
import glob

class RemoveComments:

    pass



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





# f.close()

# # Checking for Java Comments
# for txtFile in txtFiles:
#     f = open(txtFile, 'r+')
#     print(f.read())