import os
from functions.valid_path import is_valid_path
from config import *

def get_file_content(working_directory, file_path):
     try:
          # abs_path = os.path.abspath(working_directory)
          # reading_file_path = os.path.normpath(os.path.join(abs_path, file_path))
          # valid_file_path = os.path.commonpath([abs_path, reading_file_path]) == abs_path
          valid_file, target_p = is_valid_path(working_directory, file_path)

          if not valid_file:
               return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
          if not os.path.isfile(target_p):
               return f'Error: File not found or is not a regular file: "{file_path}"'

          with open(target_p, 'r') as file:
               file_content_string = file.read(MAX_CHAR)
               if file.read(1):
                    file_content_string += f'[...File "{file_path}" truncated at {MAX_CHAR} characters]'

          return file_content_string
     except Exception as e:
          return f"Error: {e}"

# get_file_content('calculator', 'lorem.txt')