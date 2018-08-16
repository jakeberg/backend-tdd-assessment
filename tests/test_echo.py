import unittest
import sys
import subprocess
import echo


class TestEcho(unittest.TestCase):

    def test_help(self):
        """ Running the program without arguments should show usage. """
    
        # Run the command `python ./echo.py -h` in a separate process, then
        # collect it's output.
        process = subprocess.Popen(
            ["python", "./echo.py", "-h"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        usage = open("./USAGE", "r").read()
    
        self.assertEquals(stdout, usage)

    def test_text(self):
        '''Tests to see what happens if only text is enter'''
        self.parser = echo.create_parser()
        args = ['hello']
        namespace = self.parser.parse_args(args)
        self.assertEquals(namespace.text, "hello")
    
    def test_none(self):
        '''Tests what happens after no text is entered'''
        process = subprocess.Popen(
            ["python", "./echo.py"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        self.assertEquals(stdout, "usage: echo.py [-h] [-u] [-l] [-t] text\n")
    
    def test_all(self):
        '''Tests what happens after if all arguments are passed'''
        process = subprocess.Popen(
            ["python", "./echo.py", "-tul", "heLLo!"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        self.assertEquals(stdout, "Hello!\n")
    
    def test_some(self):
        '''Tests what happens after if some arguments are passed'''
        process = subprocess.Popen(
            ["python", "./echo.py", "-ul", "heLLo!"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        self.assertEquals(stdout, "hello!\n")

    def test_uppercase(self):
        '''Tests uppercase'''
        process = subprocess.Popen(
            ["python", "./echo.py", "-u", "hello"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        self.assertEquals(stdout, "HELLO\n")

    def test_lowercase(self):
        '''Tests lowercase'''
        process = subprocess.Popen(
            ["python", "./echo.py", "-l", "HELLO"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        self.assertEquals(stdout, "hello\n")

    def test_titlecase(self):
        '''Tests titlecase'''
        process = subprocess.Popen(
            ["python", "./echo.py", "-t", "hello world"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        self.assertEquals(stdout, "Hello World\n")
    

if __name__ == '__main__':
    unittest.main()