from google.genai import types
from functions.get_files_info import *
from functions.get_file_contents import *
from functions.run_python_file import *
from functions.write_file_contents import *


available_functions = types.Tool(
     function_declarations=[schema_get_files_info, schema_get_file_contents, schema_run_python_file, schema_write_file_contents]
)


# function_call will be a FunctionCall Object
def call_function(function_call, verbose=False):
     function_map = {
          'get_file_contents': get_file_contents,
          'get_files_info': get_files_info,
          'run_python_file': run_python_file,
          'write_file': write_file,
     }

     if verbose:
          print(f"Calling function: {function_call.name}({function_call.args})")
     else:
          print(f" - Calling function: {function_call.name}")
     
     function_name = function_call.name or ''

     if function_map.get(function_name) == None:
          return types.Content(
               role='tool',
               parts=[
                    types.Part.from_function_response(
                         name=function_name,
                         response={'error': f'Unknown function: {function_name}'},
                    )
               ]
          )

     args = dict(function_call.args) if function_call.args else {}
     args['working_directory'] = './calculator'

     function_result = function_map[function_name](**args)

     return types.Content(
          role='tool',
          parts=[
               types.Part.from_function_response(
                    name=function_name,
                    response={'result': function_result}
               )
          ]
     )