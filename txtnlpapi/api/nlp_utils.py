from __future__ import absolute_import, unicode_literals
from textblob import TextBlob

def get_sentiment(text):
    try:
        comment_blob = TextBlob(text)
    except:
        return Exception 
    finally:
        return {
                'polarity': comment_blob.sentiment.polarity, 
                'subjectivity': comment_blob.sentiment.subjectivity
                }
