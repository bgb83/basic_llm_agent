import os
import subprocess

def run_python_file(working_directory, file_path, args=[]):
    full_path = os.path.join(working_directory,file_path)
    if working_directory not in os.path.abspath(full_path):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(full_path):
        return f'Error: File "{file_path}" not found.'
    if not full_path.endswith('.py'):
        return f'Error: "{file_path}" is not a Python file.'
    try: 
        result = subprocess.run(["python", full_path, *args],timeout =30,capture_output=True, check=True)
        
        stdout_string = f'STDOUT: {result.stdout}' 
        stderr_string = f'STDERR: {result.stderr}'
        error_string =  f'Process exited with code {result.returncode}' if result.returncode != 0 else ''
        empty_string =  '' if len(result.stdout) > 0 else "No output produced"
        
        result_string = stdout_string + stderr_string + error_string + empty_string
        
    except Exception as e:
        return f"Error: executing Python file: {e}"
    
    return result_string

