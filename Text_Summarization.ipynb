import bs4 as bs
import urllib.request as url
import re
import nltk
import heapq
from string import punctuation

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('stopwords')

from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

# Fetch Wikipedia Article
scraped_data = url.urlopen('https://en.wikipedia.org/wiki/Pope_Francis')
article = scraped_data.read()
parsed_article = bs.BeautifulSoup(article, 'lxml')
paragraphs = parsed_article.find_all('p')

# Convert article into text
article_text = " ".join([p.text for p in paragraphs])

# Text Preprocessing
article_text = re.sub(r'\[[0-9]*\]', ' ', article_text)  # Remove references
article_text = re.sub(r'\s+', ' ', article_text)  # Remove extra spaces
formatted_article_text = re.sub('[^a-zA-Z]', ' ', article_text)  # Remove special characters
formatted_article_text = re.sub(r'\s+', ' ', formatted_article_text)  # Normalize spaces

# Tokenize Sentences
sentence_list = sent_tokenize(article_text)

# Compute Word Frequencies
stopwords_set = set(stopwords.words('english'))
word_frequencies = {}

for word in word_tokenize(formatted_article_text.lower()):
    if word not in stopwords_set and word not in punctuation:
        word_frequencies[word] = word_frequencies.get(word, 0) + 1

# Normalize Word Frequencies
maximum_frequency = max(word_frequencies.values())
for word in word_frequencies:
    word_frequencies[word] /= maximum_frequency

# Calculate Sentence Scores
sentence_scores = {}

for sent in sentence_list:
    sentence_word_count = len(sent.split(' '))
    if sentence_word_count < 40:  
     # Adjusting sentence length for better readability
        for word in word_tokenize(sent.lower()):
            if word in word_frequencies:
                sentence_scores[sent] = sentence_scores.get(sent, 0) + word_frequencies[word]

# Extract Summary (Balanced Length)
summary_sentences = heapq.nlargest(8, sentence_scores, key=sentence_scores.get)

# Format Output with Dashes
print("Summary:\n")
for sent in summary_sentences:
    print(f"- {sent}")  # Adds a dash before each sentence
