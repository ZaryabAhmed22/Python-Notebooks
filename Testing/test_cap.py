import unittest
import cap

#Creating the test class
class TestCap(unittest.TestCase):

  #Defining the test method
  def test_one_word(self):
    text = 'python'

    # Saving the returned result from the cap_text function in a variable
    result = cap.cap_text(text)

    # Testing condition
    self.assertEqual(result, 'Python')

  def test_multiple_words(self):
    text = 'monty python'
    result = cap.cap_text(text)
    self.assertEqual(result, 'Monty Python')

# Makin sure that the test file is running not the cap.py
if __name__ == '__main__':
  #running the unittest
  unittest.main()