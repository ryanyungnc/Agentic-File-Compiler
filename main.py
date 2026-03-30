

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read()
    except FileNotFoundError:
        print(f"Error: the file '{file_path}' was not found")
    
    return text



def file_analysis(file_paths):
    

