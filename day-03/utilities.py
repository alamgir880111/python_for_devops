import json

def read_file(file_name):
    with open (file_name, "r") as file:
        result = file.readlines()
        return result
        
    