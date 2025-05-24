 
from sentiment import analyze_sentiment

def test_positive():
    assert analyze_sentiment("I love this product!") == "Positive"

def test_negative():
    assert analyze_sentiment("This is the worst experience ever.") == "Negative"

def test_neutral():
    assert analyze_sentiment("It's okay, not great.") == "Neutral"
