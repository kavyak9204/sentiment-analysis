 
import unittest
from sentiment import analyze_sentiment

class TestSentimentAnalysis(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(analyze_sentiment("I love this product!"), "Positive")

    def test_negative(self):
        self.assertEqual(analyze_sentiment("This is the worst experience ever."), "Negative")

    def test_neutral(self):
        self.assertEqual(analyze_sentiment("It's okay, not great."),"Negative")

if __name__ == "__main__":
    unittest.main(verbosity=2)
