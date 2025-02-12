from textblob import TextBlob

def analyze_sentiment(text):
    blob = TextBlob(text)
    return blob.sentiment.polarity

def categorize_sentiment(sentiment):
    if sentiment > 0.5:
        return "Strongly Positive", "😊"
    elif sentiment > 0:
        return "Positive", "🙂"
    elif sentiment == 0:
        return "Neutral", "😐"
    elif sentiment > -0.5:
        return "Negative", "🙁"
    else:
        return "Strongly Negative", "😡"

# Input text
input_text = "I am G Shankar from 3rd year CSE AIML. I have basic skills in programming and machine learning. I am interested in doing projects and learning new things. Thank you!"

# Perform sentiment analysis
sentiment_score = analyze_sentiment(input_text)
sentiment_category, emoji = categorize_sentiment(sentiment_score)

# Display output in Jupyter Notebook
print(f"Input Text: {input_text}")
print(f"Sentiment Score: {sentiment_score}")
print(f"Sentiment Category: {sentiment_category} {emoji}")
