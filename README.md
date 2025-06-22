## Text-Summarization-Tool

*COMPANY*: CODTECH IT SOLUTUIONS

*NAME*: MAKWANA SAKSHI M

*INTERN ID*: C0DF93

*DOMAIN*: ARTIFICIAL INTELLIGENCE MARKUP LANGUAGE

*DURATION*: 4 WEEKS

*MENTOR*: NEELA SANTHOSH


#  Text Summarization Tool  
**Efficient Extractive Summarization of Web Articles using Classical NLP Techniques**  

## Overview: 
In today's information-driven world, **text summarization** plays a crucial role in helping readers quickly grasp the essence of lengthy documents, articles, and reports. This project presents a streamlined **extractive summarization pipeline in Python**, leveraging **Natural Language Toolkit (NLTK)** alongside web scraping tools like `BeautifulSoup` and `urllib`.

This tool demonstrates its capabilities by summarizing a **Wikipedia article** (on Pope Francis), converting unstructured web content into a **concise, coherent summary**.  

## Methodology:  
The summarization pipeline follows a structured approach:  

### 1️. Data Acquisition (Web Scraping)  
The pipeline begins by fetching the target web article using Python’s `urllib` library. The raw HTML content is parsed using `BeautifulSoup`, extracting relevant textual data—specifically, content within `<p>` tags.  

### 2️. Text Preprocessing  
Several essential preprocessing steps are applied:  
- **Noise Removal**: Eliminates references (e.g., `[1]`, `[2]`), special characters, digits, and extra spaces.  
- **Normalization**: Converts text to lowercase for uniformity.  
- **Tokenization**: Splits the cleaned text into sentences and words using NLTK’s `sent_tokenize` and `word_tokenize`.  
- **Stopword Filtering**: Removes common stopwords and punctuation to retain semantically meaningful words.  

### 3️. Word Frequency Analysis  
The frequency distribution of significant words is calculated and **normalized** by dividing against the highest frequency observed.  

### 4️. Sentence Scoring and Ranking  
Each sentence is evaluated by summing the normalized frequencies of its key words.  
- Sentences with **40 words or fewer** are considered for scoring (adjusted for readability).  
- The **top 8 sentences** with the highest scores are extracted to form the summary.  

### 5️. Summary Generation and Visualization  
The extracted sentences are structured into a **bullet-point summary** for clarity. Additionally, a **word frequency distribution plot** (using Matplotlib) visually highlights the most common words in the article.  

## Requirements: 
Ensure the following Python libraries are installed:  

```bash
pip install bs4 urllib nltk heapq matplotlib
```
Additionally, download required NLTK data:  

```python
import nltk
nltk.download('punkt')
nltk.download('stopwords')
```

## Applications:  
This tool can be used for:  
- Quick summarization of lengthy articles and reports  
- Educational demonstrations of classical NLP techniques  
- Preprocessing steps for machine learning pipelines  
- Prototyping information extraction or recommendation systems  

## Future Improvements:  
- Make URL input **fully dynamic** for any article  
- Expand support for **multiple languages**  
- Integrate **Named Entity Recognition (NER)** for smarter sentence selection  
- Explore **TF-IDF or Latent Semantic Analysis (LSA)** to enhance summary quality  
- Implement **abstractive summarization with deep learning (Transformers, BERT)**  
- Allow document summarization from **local files (PDF, DOCX, TXT)**  

## Output:
![Image](https://github.com/user-attachments/assets/28a89729-530f-428f-ae1b-1f56ccb680d7)
