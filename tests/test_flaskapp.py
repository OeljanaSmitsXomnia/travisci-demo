import unittest

from main import multiply, hello, to_uppercase

class MyTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_multiply(self):
        #given
        x = 10
        y = 12

        #when
        answer = multiply(x,y)

        #then
         self.assertEqual(answer, 120)
   
if __name__ == '__main__':
    unittest.main()