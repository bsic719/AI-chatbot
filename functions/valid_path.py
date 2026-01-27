import os

def is_valid_path(working_path, target_path):
     current_p = os.path.abspath(working_path)
     target_p = os.path.normpath(os.path.join(current_p, target_path))

     valid_p = os.path.commonpath([current_p, target_p]) == current_p
     return valid_p, target_p
