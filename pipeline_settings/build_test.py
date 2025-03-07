import unittest

class TestIndexFile(unittest.TestCase):

    def test_hello(self):
        with open('pipeline_settings/index.py', 'r') as file:
            code = file.read()
        self.assertIn('Hello', code)

if __name__ == '__main__':
    unittest.main()
