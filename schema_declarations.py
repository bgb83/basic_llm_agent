from google.genai import types

schema_get_files_info = types.FunctionDeclaration(
        name="get_files_info",
        description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
        parameters=types.Schema(
            type=types.Type.OBJECT,
            properties={
                "directory": types.Schema(
                    type=types.Type.STRING,
                    description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
                ),
            },
        ),
    )

schema_get_file_content = types.FunctionDeclaration(
        name="get_file_content",
        description="gets specified file's content as a string truncated to 10000 characters, constrained to the working directory.",
        parameters=types.Schema(
            type=types.Type.OBJECT,
            properties={
                "file_path": types.Schema(
                    type=types.Type.STRING,
                    description="The file path to the file to get content from, relative to working directory.",
                ),
            },
        ),
    )

schema_run_python_file = types.FunctionDeclaration(
        name="run_python_file",
        description="runs  python file, accepts arguments, constrained to the working directory.",
        parameters=types.Schema(
            type=types.Type.OBJECT,
            properties={
                "file_path": types.Schema(
                    type=types.Type.STRING,
                    description="The file path to the file to get content from, relative to working directory.",
                ),
                "args": types.Schema(
                    type=types.Type.OBJECT,
                    description="Input arguments that the python file needs to run provided as a list",
                ),
            },
        ),
    )

schema_write_file = types.FunctionDeclaration(
        name="write_file",
        description="writes content to a specified file, constrained to the working directory.",
        parameters=types.Schema(
            type=types.Type.OBJECT,
            properties={
                "file_path": types.Schema(
                    type=types.Type.STRING,
                    description="The file path to the file to be written, relative to working directory.",
                ),
                "content": types.Schema(
                    type=types.Type.STRING,
                    description="The content to be written to the file",
                ),
            },
        ),
    )