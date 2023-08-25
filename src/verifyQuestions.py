import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load NLTK resources
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Preprocessing functions
def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    tokens = word_tokenize(text)
    tokens = [token for token in tokens if token not in stopwords.words('english')]
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(token) for token in tokens]
    return ' '.join(tokens)

# Load and preprocess the question base
with open('./assets/test.txt', 'r') as file:
    question_base = file.readlines()

question_base = [preprocess_text(question) for question in question_base]

# TF-IDF vectorization
vectorizer = TfidfVectorizer()
question_base_tfidf = vectorizer.fit_transform(question_base)

# User input
user_question = input("Please enter a question: ")
user_question = preprocess_text(user_question)

# TF-IDF vectorization for user question
user_question_tfidf = vectorizer.transform([user_question])

# Calculate cosine similarities
similarities = cosine_similarity(user_question_tfidf, question_base_tfidf).flatten()

# Find the most similar question
most_similar_index = similarities.argmax()
threshold = 0.4  # You can adjust this threshold as needed

if similarities[most_similar_index] > threshold:
    matching_question = question_base[most_similar_index]
    print("Similar question found in the base:")
    print(matching_question)
else:
    print("No similar question found in the base.")
