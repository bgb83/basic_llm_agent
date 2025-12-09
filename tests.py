# tests.py

import unittest
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content, MAX_CHARS
from functions.write_file import write_file

# class TestFilesInfo(unittest.TestCase):

#     def test_current(self):
#         result = get_files_info("calculator", ".")
#         expected = """- tests.py: file_size=1342 bytes, is_dir=False\n- main.py: file_size=729 bytes, is_dir=False\n- pkg: file_size=160 bytes, is_dir=True\n"""
#         self.assertEqual(result, expected)
#         print(result)

#     def test_pkg(self):
#         result = get_files_info("calculator", "pkg")
#         expected = """- render.py: file_size=388 bytes, is_dir=False\n- calculator.py: file_size=1737 bytes, is_dir=False\n"""
#         self.assertEqual(result, expected)
#         print(result)

#     def test_outside_dir(self):
#         result = get_files_info("calculator", "/bin")
#         expected = 'Error: Cannot list "/bin" as it is outside the permitted working directory'
#         self.assertEqual(result, expected)
#         print(result)

#     def test_other_outside_dir(self):
#         result = get_files_info("calculator", "../")
#         expected = 'Error: Cannot list "calculator/../" as it is outside the permitted working directory'
#         self.assertEqual(result, expected)
#         print(result)
        
# class TestContentInfo(unittest.TestCase):
    # def test_lorem(self):
    #     result = get_file_content("calculator", "lorem.txt")
    #     contains = '[...File "lorem.txt" truncated at 10000 characters]'
    #     truncate = result.replace(contains,'')
    #     self.assertTrue(result.endswith(contains))
    #     self.assertTrue(len(truncate) <= MAX_CHARS)
    
    # def test_main(self): 
    #     result = get_file_content("calculator", "main.py")
    #     self.assertTrue(len(result) <= MAX_CHARS)
    #     print(result)
        
    # def test_calculator(self):
    #     result = get_file_content("calculator", "pkg/calculator.py")
    #     self.assertTrue(len(result) <= MAX_CHARS)
    #     print(result)
        
    # def test_bin(self):
    #     result = get_file_content("calculator", "/bin/cat")
    #     expected = 'Error: Cannot read "/bin/cat" as it is outside the permitted working directory'
    #     self.assertEqual(result, expected)
    #     print(result)
        
    # def test_does_not_exist(self):
    #     result = get_file_content("calculator", "pkg/does_not_exist.py")
    #     expected = 'Error: File not found or is not a regular file: "pkg/does_not_exist.py"'
    #     self.assertEqual(result, expected)
    #     print(result)

class TestWriteContent(unittest.TestCase):
    def test_existing(self):
        result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
        content = "wait, this isn't lorem ipsum"
        expected = f'Successfully wrote to "lorem.txt" ({len(content)} characters written)'
        self.assertEqual(result, expected)
        print(result)
        
    def test_new(self):
        result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
        content = "lorem ipsum dolor sit amet"
        expected = f'Successfully wrote to "pkg/morelorem.txt" ({len(content)} characters written)'
        self.assertEqual(result, expected)
        print(result)
    
    def test_error(self):
        result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
        expected = 'Error: Cannot write to "/tmp/temp.txt" as it is outside the permitted working directory'
        self.assertEqual(result, expected)
        print(result)

    
if __name__ == "__main__":
    unittest.main()