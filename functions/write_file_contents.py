import os
from functions.valid_path import is_valid_path
from google.genai import types

schema_write_file_contents = types.FunctionDeclaration(
     name='write_file',
     description='Locate a file and write/overwrite its contents',
     parameters=types.Schema(
          type=types.Type.OBJECT,
          properties={
               'file_path':types.Schema(
                    type=types.Type.STRING,
                    description='the path to the file we are locating to write over if appropriate'
               ),
               'content':types.Schema(
                    type=types.Type.STRING,
                    description='if provided, it is the content we are writing into the file, otherwise the default content will be "hi"'
               )
          },
          required=['file_path']
     )
)

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
