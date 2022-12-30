import nltk
import numpy as np
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from scipy.spatial.distance import cosine

# Create a list of documents
documents = ["sunshine state enjoy sunshine",
             "brown fox jump high, brown fox run",
             "sunshine state fox run fast"]

# Create a list of stop words
stop_words = set(stopwords.words("english"))

# Create a stemmer
stemmer = PorterStemmer()

# Create a function to tokenize and stem the documents
def tokenize_and_stem(text):

    # Tokenize the text
    tokens = nltk.word_tokenize(text)
    
    # Remove stop words and comma
    tokens = [token for token in tokens if (token not in stop_words) and token != ',']
    
    # Stem the tokens
    stems = [stemmer.stem(token) for token in tokens]
    
    return stems

# Create a CountVectorizer object
vectorizer = CountVectorizer(tokenizer=tokenize_and_stem)

# Create the bag of words matrix
bag_of_words = vectorizer.fit_transform(documents)

# Create TF Matrix 
data_for_TF = bag_of_words.toarray()

Term_Frequency_Matrix = []

for TFdata in data_for_TF :
    Total_Terms_in_Array = 0
    
    for item in TFdata :
        Total_Terms_in_Array =+ item
    Term_Frequency_Array = []
    for item in TFdata :
        Term_Frequency_Array.append(item/Total_Terms_in_Array)
    Term_Frequency_Matrix.append(Term_Frequency_Array)    

# Create a TfidfVectorizer object
vectorizer2 = TfidfVectorizer()

# Create the TF-IDF matrix
tfidf_matrix = vectorizer2.fit_transform(documents)

# Print the vocabulary
print(vectorizer.vocabulary_)
# Print the bag of words matrix
print("BAG OF WORDS MATRIX")
print(bag_of_words.toarray())

# Print the Term Frequency matrix
print("TERM FREQUENCY MATRIX")
print(Term_Frequency_Matrix)

# Print the TF-IDF matrix
print("TF-IDF MATRIX")
print(tfidf_matrix.toarray())

vector1 = (tfidf_matrix.toarray())[1]
vector2 = (tfidf_matrix.toarray())[0]

cosine_angle = cosine(vector1, vector2)

print(cosine_angle)
