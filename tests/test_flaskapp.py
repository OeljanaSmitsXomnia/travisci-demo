import unittest

from main import multiply, hello, to_uppercase

class MyTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_multiply(self):
        #given
        x = "10"
        y = "12"

        #when
        answer = multiply(x,y)

        #then
        with self.assertRaises(typeError):
            answer = multiply(x,y)

    def test_to_upper(self):
        # given
        s = 'hi'

        # when
        answer = to_uppercase(s)

        # then
        self.assertEqual(answer, 'HI')

    def test_hello(self):
        # given

        # when
        answer = hello()

        # then
        self.assertEqual("Hello World!")



if __name__ == '__main__':
    unittest.main()