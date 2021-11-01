from textblob import TextBlob
import nltk
from pathlib import Path
import pandas as pd 
nltk.download("stopwords")
from nltk.corpus import stopwords
from operator import itemgetter
import pandas as pd
import matplotlib.pyplot as plt

stops = stopwords.words('english')
blob = TextBlob("Today is a beautiful day")
cleanlist = [word for word in blob.words if word not in stops]

blob = TextBlob(Path("book of john text.txt").read_text())
print(blob.words.count("joy"))
print(blob.word_counts["juliet"])
#print(blob.noun_phrases.count("lady capulet"))
print(blob.words.count("thou"))
more_stops = ["thy", "ye", "verily", "thee", "hath", "say", "thou", "art", "shall"]
stops += more_stops
items = blob.nouns_counts.items()
#print(items)

clean_items = [i for i in items if i[0] not in stops]
print(clean_items[:10])
sorted_list = sorted(clean_items,key=itemgetter(1),reverse=True)
print(sorted_list[:10])

top20 = sorted_list[:20]

df = pd.DataFrame(top20, columns=["word","count"])
print(df)