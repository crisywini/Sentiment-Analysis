from textblob import TextBlob
from transformers import pipeline

classifier = pipeline('sentiment-analysis')

text = input()
blob = TextBlob(text)
x_blob = blob.sentiment
x_pipe = classifier(text)
print(x_blob)
print(x_pipe)