import os
import glob

os.system("touch sample_folder/file1.txt && touch sample_folder/file2.txt")

f1 = open("sample_folder/file1.txt", 'w')
f2 = open("sample_folder/file2.txt", 'w')

textList = ['data', '// comment']

# Opening all txtFiles
txtFiles = glob.glob('**/*.txt', recursive=True)

for line in textList:
    f1.write(line)
    f1.write("\n")
    f2.write(line)
    f2.write("\n")    

for txtFile in txtFiles:
    f = open(txtFile, 'a+')
    f.write("hey")
f.close()

# Checking for Java Comments
for txtFile in txtFiles:
    f = open(txtFile, 'r+')
    print(f.read())