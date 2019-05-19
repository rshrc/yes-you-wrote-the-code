import re
import glob

class FileManager:

    def __init__(self, file_type):
        self.file_type = '**/*.' + file_type
        print("Extracting all .", self.file_type, " files")
        self.txtFiles = glob.glob(self.file_type, recursive=True)
        if not self.txtFiles:
            print("Found None!")
        print(self.txtFiles)

    def traverse_and_replace(self):
        for txtFile in self.txtFiles:
            f = open(txtFile, 'r+')
            file_content = str(f.read())
            if self.file_type == 'css':
                file_content = self.remove_comments_css_style(file_content)
            elif self.file_type == 'html':
                file_content = self.remove_comments_html_style(file_content)
            else:
                file_content = self.remove_comments_c_style(file_content)
            f.close()
            f = open(txtFile, 'w')
            f.write(str(file_content).strip())
            f.close()
    
    def remove_comments_c_style(self, string):
        string = re.sub(re.compile("/\*.*?\*/",re.DOTALL ) ,"" ,string)
        string = re.sub(re.compile("//.*?\n" ) ,"" ,string) 
        return string
    
    def remove_comments_css_style(self, string):
        string = re.sub(re.compile("(/\*([^*]|[\r\n]|(\*+([^*/]|[\r\n])))*\*+/)", re.DOTALL), "", string)
        return string

    def remove_comments_html_style(self, string):
        string = re.sub(re.compile("<!--(.*?)-->"), "", string)
        return string