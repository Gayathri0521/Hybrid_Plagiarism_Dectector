import pytesseract
from PIL import Image
import nltk
import string

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer

# Download nltk
nltk.download('punkt')
nltk.download('stopwords')

# Load Model
model = SentenceTransformer('all-MiniLM-L6-v2')

stop_words = set(stopwords.words('english'))

# Text Preprocessing
def preprocess(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))

    words = word_tokenize(text)
    words = [word for word in words if word not in stop_words]

    return " ".join(words)

# Extract Text
def extract_text(file):

    filename = file.name.lower()

    if filename.endswith((".png", ".jpg", ".jpeg")):
        image = Image.open(file)
        text = pytesseract.image_to_string(image)

    else:
        text = file.read().decode("utf-8")

    return text

# Similarity Function
def compute_similarity(text1, text2):

    text1 = preprocess(text1)
    text2 = preprocess(text2)

    # TF-IDF
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([text1, text2])

    tfidf_score = cosine_similarity(tfidf_matrix[0], tfidf_matrix[1])[0][0]

    # BERT
    embeddings = model.encode([text1, text2])

    bert_score = cosine_similarity(
        [embeddings[0]],
        [embeddings[1]]
    )[0][0]

    final_score = (tfidf_score + bert_score) / 2

    return tfidf_score, bert_score, final_score