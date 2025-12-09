import os

def get_files_info(working_directory, directory="."):
    dir_path = os.path.join(working_directory, directory)
    if working_directory not in os.path.abspath(dir_path):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(dir_path):
        return f'Error: "{directory}" is not a directory'
        
    files = ''
    for file in os.listdir(dir_path):
        if not file.startswith('_'):
            file_path = os.path.join(dir_path,file)
            files += f'- {file}: file_size={os.path.getsize(file_path)} bytes, is_dir={os.path.isdir(file_path)}\n'
        
    return files