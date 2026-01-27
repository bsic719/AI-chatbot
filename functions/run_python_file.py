import os
from functions.valid_path import is_valid_path
import subprocess

def run_python_file(working_directory='calculator', file_path='main.py', args=None):
     try:
          absolute_file_p = os.path.abspath(working_directory)
          is_valid, target_p = is_valid_path(working_directory, file_path)

          if not is_valid:
               return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
          if not os.path.isfile(target_p):
               return f'Error: "{file_path}" does not exist or is not a regular file'
          if not target_p.endswith('.py'):
               return f'Error: "{file_path}" is not a Python file'
          
          # fixing target_p to be the cwd as intended
          command=['python', target_p]

          if args:
               command.extend(args)

          result = subprocess.run(command, capture_output=True, text=True, timeout=30, cwd=working_directory)

          message = []
          if result.returncode:
               message.append('Process exited with code X')
          if not result.stdout and not result.stderr:
               message.append('No output produced')

          if result.stdout:
               message.append(f"STDOUT: {result.stdout}")
          if result.stderr:
               message.append(f"STDERR: {result.stderr}")

          return '\n'.join(message)

     except Exception as e:
          return f"Error: executing Python file: {e}"
     