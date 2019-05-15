from textblob import TextBlob

class SentimentAnalyzer():
    def __init__(self, text):
        self.text = text
    
    def get_sentiment(self):
        try:
            comment_blob = TextBlob(self.text)
        except:
            return Exception 
        finally:
            return {
                    'polarity': comment_blob.sentiment.polarity, 
                    'subjectivity': comment_blob.sentiment.subjectivity
                    }
