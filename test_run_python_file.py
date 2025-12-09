import unittest
from functions.run_python_file import run_python_file

class TestRunPythonFiles(unittest.TestCase):

    def test_calculator_file(self):
        result = run_python_file("calculator", "main.py")
        self.assertIn("Calculator App", result)
        self.assertIn('Usage: python main.py "<expression>"', result)
        self.assertIn('Example: python main.py "3 + 5"', result)
        print(result)
        
    def test_calculator_args(self):
        result = run_python_file("calculator", "main.py", ["3 + 5"])
        self.assertIn('"result": 8', result)
        print(result)
        
    def test_calculator_test(self):
        result = run_python_file("calculator", "tests.py")
        self.assertIn('OK', result)
        self.assertIn('Ran 9 tests', result)
        print(result)
        
    def test_wrong_path(self):
        result = run_python_file("calculator", "../main.py")
        error_msg = f'Error: Cannot execute "../main.py" as it is outside the permitted working directory'
        self.assertIn(error_msg, result)
        print(result)
        
    def test_nonexistent_file(self):
        result = run_python_file("calculator", "nonexistent.py")
        error_msg = f'Error: File "nonexistent.py" not found.'
        self.assertIn(error_msg, result)
        print(result)
        
    def test_wrong_file(self):
        result = run_python_file("calculator", "lorem.txt")
        error_msg = f'Error: "lorem.txt" is not a Python file.'
        self.assertIn(error_msg, result)
        print(result)
        
if __name__ == "__main__":
    unittest.main()