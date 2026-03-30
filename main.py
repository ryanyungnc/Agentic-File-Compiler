import os
import json
from google import genai
from google.genai import types
from dotenv import load_dotenv

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read()
    except FileNotFoundError:
        print(f"Error: the file '{file_path}' was not found")
    
    return text



def file_analysis(file_paths):
    content = []
    
    for file_path in file_paths:
        text = read_file(file_path)
        content.append(text)
    
