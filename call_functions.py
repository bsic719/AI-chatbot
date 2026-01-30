from google.genai import types

schema_get_files_info = types.FunctionDeclaration(
     name='get_files_info',
     description='Lists files in a specific directory relative to the working directory, providing file size and directory status',
     parameters=types.Schema(
          type=types.Type.OBJECT,
          properties={
               'directory': types.Schema(
                    type=types.Type.STRING,
                    description='Directory path to list files from, relative to the working directory (default is the working directory itself)',
               ),

          },
     ),
)

schema_get_file_contents = types.FunctionDeclaration(
     name='get_file_contents',
     description='Can read the contents in a specific file relative to the working directory, providing the contents up to a certain number of characters',
     parameters=types.Schema(
          type=types.Type.OBJECT,
          properties={
               'file_path': types.Schema(
                    type=types.Type.STRING,
                    description='Directory path to the file we want to read the contents from, relative to the working directory (default is the working directory itself)',
               )
          },
          required=['file_path'],
     )
)

schema_run_python_file = types.FunctionDeclaration(
     name='run_python_file',
     description='Execute the python file in a specific working path if appropriate',
     parameters=types.Schema(
          type=types.Type.OBJECT,
          properties={
               "file_path":types.Schema(
                    type=types.Type.STRING, 
                    description='The path to the file that we want to run if it is a python file relative to the working directory'
               ),
               "args":types.Schema(
                    type=types.Type.ARRAY,
                    items=types.Schema(
                         type=types.Type.STRING,
                         description='this is the parameter we are passing as an arg to be added to command if there are any'
                    ),
                    description='The array that will be extended to the command if any, otherwise nothing is added to command'
               )
          },
          required=['file_path']
     )
)

schema_write_file_contents = types.FunctionDeclaration(
     name='write_file_contents',
     description='write contents into a specific file',
     parameters=types.Schema(
          type=types.Type.OBJECT,
          properties={
               'file_path':types.Schema(
                    type=types.Type.STRING,
                    description='path to the file that we want to write contents into'
               ),
               'contents':types.Schema(
                    type=types.Type.STRING,
                    description='the content we want to write into the file_path'
               )
          }
     )
)