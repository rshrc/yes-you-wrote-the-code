from utils import FileManager
from parser import get_station_parser

args = get_station_parser()

file_type = input("Enter File Type you want to strip : ")

fm = FileManager(file_type)
fm.traverse_and_replace()
print("Done!")
