import os
from functions.valid_path import is_valid_path
from google.genai import types

# Gemini API standard to call get_files_info()
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

def get_files_info(working_directory, directory='.'):
     try:
          # helper fn to check if target_path is within working path
          valid_dir, target_path = is_valid_path(working_directory, directory)


          if directory == '.':
               print(f"Result for current directory")
          else:
               print(f"Result for '{directory}' directory")
          
          if not valid_dir:
               return f'    Error: Cannot list "{directory}" as it is outside the permitted working directory'

          if not os.path.isdir(target_path):
               return f'    Error: "{directory}" is not a directory'
          
          files_in_dir = os.listdir(target_path)
          detailed_infos = []
          for file in files_in_dir:
               cur_file_path = os.path.join(target_path, file)
               detailed_infos.append(f"  - {file}: file_size={os.path.getsize(cur_file_path)} bytes, is_dir={os.path.isdir(cur_file_path)}")
          
          return "\n".join(detailed_infos)

     except Exception as e:
          return f"Error: {e}"

# def get_files_info(working_directory, directory='.'):
#      # abs path of working directory
#      absolute_path = os.path.abspath(working_directory)
#      target_dir = os.path.normpath(os.path.join(absolute_path, directory))

#      valid_target_dir = os.path.commonpath([target_dir, absolute_path]) == absolute_path
#      return_info = []
#      print(f"Result for '{directory} directory:")

#      if not valid_target_dir:
#           return f'    Error: Cannot list "{directory}" as it is outside the permitted working directory'

#      if not os.path.isdir(target_dir):
#           return f"    Error: '{directory}' is not a directory"

#      files_in_target = os.listdir(target_dir)
#      for file in files_in_target:
#           file_path = os.path.join(target_dir, file)
#           return_info.append(f"  - {file}: file_size={os.path.getsize(file_path)} bytes, is_dir={os.path.isdir(file_path)}")

#      return '\n'.join(return_info)

