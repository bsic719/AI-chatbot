import os
from functions.valid_path import is_valid_path

def write_file(working_directory, file_path, content='hi'):
     try:
          is_valid, target_p = is_valid_path(working_directory, file_path)

          if not is_valid:
               return f"Error: Cannot write to '{file_path}' as it is outside the permitted working directory"
          if os.path.isdir(target_p):
               return f'Error: Cannot write to "{file_path}" as it is a directory'

          os.makedirs(os.path.dirname(target_p), exist_ok=True)

          with open(target_p, 'w') as file:
               file.write(content)
               return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
     except Exception as e:
          return f"Error: {e}"
