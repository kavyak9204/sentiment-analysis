
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

# Download VADER lexicon (only first time)
nltk.download('vader_lexicon')

def analyze_sentiment(text):
    sid = SentimentIntensityAnalyzer()
    score = sid.polarity_scores(text)
    if score['compound'] >= 0.05:
        return "Positive"
    elif score['compound'] <= -0.05:
        return "Negative"
    else:
        return "Neutral"

if __name__ == "__main__":
    user_input = input("Enter text to analyze sentiment: ")
    result = analyze_sentiment(user_input)  # <-- Use user's input
    print("Sentiment:", result)             # <-- Removed comma
