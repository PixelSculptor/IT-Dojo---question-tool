import json
import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from configModel import configModel
from getAnswer import get_definition
from translateFlashcards import translateQuestionPack

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
result_path = input("Please choose result path for your files: ")

# Load and preprocess the question base
with open(question_base_path, 'r') as file:
    question_base = file.readlines()

question_base = [preprocess_text(question) for question in question_base]

# TF-IDF vectorization
vectorizer = TfidfVectorizer()
question_base_tfidf = vectorizer.fit_transform(question_base)


# Function to check similarity and add to base
def check_similarity_and_add(candidate_question):
    candidate_question_preprocessed = preprocess_text(candidate_question)
    candidate_question_tfidf = vectorizer.transform([candidate_question_preprocessed])

    # Calculate cosine similarities
    similarities = cosine_similarity(candidate_question_tfidf, question_base_tfidf).flatten()

    # Find the most similar question
    most_similar_index = similarities.argmax()
    threshold = 0.5  # You can adjust this threshold as needed

    if similarities[most_similar_index] > threshold:
        matching_question = question_base[most_similar_index]
        print(f"Similar question found in the base for candidate: {candidate_question}")
        print(f"Matching question: {matching_question}")
        with open(result_path + '/errorlog.txt', 'w') as errorlog:
            errorlog.write(candidate_question.strip() + '\n')
        with open('./assets/questions-suspected.txt', 'w') as file:
            file.write(
                'Pattern question: ' + matching_question.strip() + '\n' + 'Suspected question: ' + candidate_question.strip() + '\n')
    else:
        print(f"No similar question found in the base for candidate: {candidate_question}")
        add_to_base = input("Do you want to add this question to the base? (yes/no): ")
        if add_to_base.lower() == 'yes':
            question_base.append(candidate_question_preprocessed)
            with open(question_base_path, 'a') as file:
                file.write(candidate_question.strip() + '\n')
            print("Question added to the base.")


# Read and process candidate questions
with open(result_path + '/candidates.txt', 'r') as candidates_file:
    candidates = candidates_file.readlines()

for candidate in candidates:
    candidate = candidate.strip()
    check_similarity_and_add(candidate)

userContext = input("Choose a context for LLM model between frontend and QA: ").lower()

def writeDefintions(userContextChoice):
    context = configModel(userContextChoice)
    listOfDefinitions = []
    # request to model
    for question in question_base:
        definition = get_definition(context, question)
        questionPair = {
            "question": question,
            "answer": definition
        }
        print("typing answer...")
        listOfDefinitions.append(questionPair)

    # write list to json file
    with open(result_path + '/definitions-eng.json', 'w') as definitions:
        definitions.write(json.dumps(listOfDefinitions, indent=4))


# run function that will generate answers
writeDefintions(userContext)

# translate into Polish
translateQuestionPack(result_path)

print("Exiting the script.")
