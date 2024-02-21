import nltk
nltk.download('punkt')

from nltk.tokenize import sent_tokenize

text="Tokenization is the first step in text 101 analytics. The process of breaking down a text paragraph into smaller chunks such as words or sentence is called Tokenization. Token is a single entity that is building blocks for sentence or paragraph."
tokenized_text=sent_tokenize(text)
print(tokenized_text)

from nltk.tokenize import word_tokenize
tokenized_word=word_tokenize(text)
print(tokenized_word)

nltk.download('stopwords')
from nltk.corpus import stopwords
stop_words=set(stopwords.words("english"))
print(stop_words)

filtered_sent=[]
for w in tokenized_word:
    if w not in stop_words:
        filtered_sent.append(w)
print("Tokenized Sentence:",tokenized_word)
print("Filterd Sentence:",filtered_sent)

words = [w for w in filtered_sent if w.isalpha()]
words

from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize

ps = PorterStemmer()

stemmed_words=[]
for w in words:
    stemmed_words.append(ps.stem(w))

print("Filtered Sentence:",words)
print("Stemmed Sentence:",stemmed_words)



