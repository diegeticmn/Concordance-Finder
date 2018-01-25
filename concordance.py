import re
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
from nltk import ngrams
from collections import Counter
import string
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk import Text

text = ''

for i in range(YOUR RANGE LOWER BOUND HERE AS INTEGER, YOUR RANGE UPPER BOUND HERE AS INTEGER):
	with open('YOUR FILE TEMPLATE HERE.txt'.format(i)) as f:
		text += f.read().replace('\n', ' ')

text = text.lower()

tokens = word_tokenize(text)
textList = Text(tokens)
textList.concordance('election', lines=99999)
