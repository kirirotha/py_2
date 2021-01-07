import unittest
import simple2


class TestSimple2(unittest.TestCase):

    def test_one_word(self):
        text = 'python'
        result = simple2.cap_text(text)
        self.assertEqual(result,'Python')

    def test_multiple_words(self):
        text = 'monty python'
        result = simple2.cap_text(text)
        self.assertEqual(result,'Monty Python')

if  __name__ == '__main__':
    unittest.main
