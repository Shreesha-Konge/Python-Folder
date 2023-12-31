import unittest
import cap

class TestCap(unittest.TestCase):

    def test_one_word(self):
        text='python'
        result=cap.cap_text(text)
        self.assertEqual(result,'Python')

    def multiple_words(self):
        text='hello python am shreesha'
        result=cap.cap_text(text)
        self.assertEqual(result,'Hello Python Am Shreesha')
        
if __name__=='__main__':
    unittest.main()
