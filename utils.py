import re
import glob

class FileManager:

    def __init__(self):
        self.txtFiles = glob.glob('**/*.txt', recursive=True)
        print(self.txtFiles)

    def traverse_and_replace(self):
        for txtFile in self.txtFiles:
            f = open(txtFile, 'r+')
            file_content = str(f.read())
            print("File Content : ", str(file_content))
            file_content = self.remove_comments(file_content)
            f.close()
            f = open(txtFile, 'w')
            f.write(str(file_content).strip())
            f.close()
    
    def remove_comments(self, string):
        string = re.sub(re.compile("/\*.*?\*/",re.DOTALL ) ,"" ,string) # remove all occurrences streamed comments (/*COMMENT */) from string
        string = re.sub(re.compile("//.*?\n" ) ,"" ,string) # remove all occurrence single-line comments (//COMMENT\n ) from string
        return string