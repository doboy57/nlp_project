from textblob import TextBlob
text = "i love you mom"
blob = TextBlob(text)
'''
print(blob.sentences)
print(blob.words)
print(blob.tags)
'''
ryan = blob.sentences
#print(blob.noun_phrases)



print(round(blob.sentiment.polarity,2))
print(round(blob.sentiment.subjectivity,3))
              
for n in ryan:
    print(n)
    print(n.sentiment.polarity)
from textblob.sentiments import NaiveBayesAnalyzer
blob = TextBlob(text, analyzer=NaiveBayesAnalyzer())
print(blob.sentiment)

for sentence in blob.sentences:
    print(sentence.sentiment)

spanish = blob.translate(to='vi')
print(spanish)