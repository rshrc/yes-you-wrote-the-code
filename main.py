from utils import FileManager

file_type = input("Enter File Type you want to strip : ")

fm = FileManager(file_type)
fm.traverse_and_replace()
print("Done!")
