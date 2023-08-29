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
    text = re.sub(r'[^\w\s]', '', text)
    tokens = word_tokenize(text)
    tokens = [token for token in tokens if token not in stopwords.words('english')]
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(token) for token in tokens]
    return ' '.join(tokens)

# ask user for path:
question_base_path = input("Please enter the path to the question base text file: ")

# Load and preprocess the question base
with open(question_base_path, 'r') as file:
    question_base = file.readlines()

question_base = [preprocess_text(question) for question in question_base]

# TF-IDF vectorization
vectorizer = TfidfVectorizer()
question_base_tfidf = vectorizer.fit_transform(question_base)

while True:
    # User input
    user_question = input("Please enter a question (or type 'exit' to quit): ")

    if user_question.lower() == 'exit':
        break

    user_question_preprocessed = preprocess_text(user_question)
    user_question_tfidf = vectorizer.transform([user_question_preprocessed])

    # Calculate cosine similarities
    similarities = cosine_similarity(user_question_tfidf, question_base_tfidf).flatten()

    # Find the most similar question
    most_similar_index = similarities.argmax()
    threshold = 0.3  # You can adjust this threshold as needed

    if similarities[most_similar_index] > threshold:
        matching_question = question_base[most_similar_index]
        print("Similar question found in the base:")
        print(matching_question)
    else:
        print("No similar question found in the base.")
        add_to_base = input("Do you want to add this question to the base? (yes/no): ")
        if add_to_base.lower() == 'yes':
            question_base.append(user_question_preprocessed)
            with open(QUESTION_BASE, 'a') as file:
                file.write(user_question + '\n')
            print("Question added to the base.")

print("Exiting the script.")


# Okay now add another feature. Instead of adding question candidate by user add function that:
# - ask user for add path to txt file with list of candidates