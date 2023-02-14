import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

def analyze(user_input):
    sia = SentimentIntensityAnalyzer()
    return sia.polarity_scores(user_input)


def main():
    # Ask for user input
    while 1:
        # Make the input text green
        user_input = input("Tell me something: ")
        analysis = analyze(user_input)
        print(analysis)


main()

