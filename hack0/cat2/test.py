import unittest
from subprocess import call
from solution import cat2

class CatTest(unittest.TestCase):
    def setUp(self):
        self.first_file_name = "test_file_1"
        self.first_file = open(self.first_file_name,"w")
        self.second_file_name = "test_file_2"
        self.second_file = open(self.second_file_name,"w")

    def test_with_two_files(self):
        self.first_file.write("Python is awesome!")
        self.first_file.close()
        self.second_file.write("Also, you can use Python at a lot of different places!")
        self.second_file.close()
        result = "Python is awesome!\n\nAlso, you can use Python at a lot of different places!"
        self.assertEqual(result,cat2([self.first_file_name,self.second_file_name]))


if __name__ == '__main__':
    unittest.main()