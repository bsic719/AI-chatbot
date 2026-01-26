import os

def write_file(working_directory, file_path, content='hi'):
     try:
          abs_path = os.path.abspath(working_directory)
          reading_file_path = os.path.normpath(os.path.join(abs_path, file_path))
          valid_path = os.path.commonpath([abs_path, reading_file_path]) == abs_path

          if not valid_path:
               return f"Error: Cannot write to '{file_path}' as it is outside the permitted working directory"
          if os.path.isdir(reading_file_path):
               return f'Error: Cannot write to "{file_path}" as it is a directory'

          os.makedirs(os.path.dirname(reading_file_path), exist_ok=True)

          with open(reading_file_path, 'w') as file:
               file.write(content)
               return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
     except Exception as e:
          return f"Error: {e}"


print(write_file('functions', 'nested_functions/get_file_contents.txt'))