"""
==========================================================
AI Resume Matcher
==========================================================

Features

1. Text Preprocessing
2. TF-IDF Vectorization
3. Cosine Similarity
4. ATS Score
5. Keyword Extraction

==========================================================
"""

import re
import nltk

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# ==========================================================
# DOWNLOAD NLTK DATA
# ==========================================================

import nltk

resources = [
    ("tokenizers/punkt", "punkt"),
    ("tokenizers/punkt_tab", "punkt_tab"),
    ("corpora/stopwords", "stopwords"),
]

for path, package in resources:
    try:
        nltk.data.find(path)
    except LookupError:
        nltk.download(package)


# ==========================================================
# TEXT PREPROCESSING
# ==========================================================

def preprocess(text):

    text = text.lower()

    text = re.sub(r"[^a-zA-Z ]", " ", text)

    words = word_tokenize(text)

    words = [

        word

        for word in words

        if word not in STOP_WORDS

        and len(word) > 1

    ]

    return " ".join(words)


# ==========================================================
# RESUME MATCH SCORE
# ==========================================================

def calculate_similarity(resume_text, job_description):

    documents = [

        resume_text,

        job_description

    ]

    vectorizer = TfidfVectorizer()

    tfidf = vectorizer.fit_transform(documents)

    similarity = cosine_similarity(

        tfidf[0:1],

        tfidf[1:2]

    )[0][0]

    percentage = round(similarity * 100, 2)

    return percentage


# ==========================================================
# ATS SCORE
# ==========================================================

def calculate_ats_score(match_percentage):

    score = min(

        round(match_percentage + 10, 2),

        100

    )

    return score


# ==========================================================
# KEYWORD EXTRACTION
# ==========================================================

def extract_keywords(text, top_n=20):

    vectorizer = TfidfVectorizer(

        stop_words="english"

    )

    matrix = vectorizer.fit_transform([text])

    scores = zip(

        vectorizer.get_feature_names_out(),

        matrix.toarray()[0]

    )

    keywords = sorted(

        scores,

        key=lambda x: x[1],

        reverse=True

    )

    return [

        word

        for word, score in keywords[:top_n]

    ]


# ==========================================================
# ANALYSIS
# ==========================================================

def analyze_resume(resume_text, job_description):

    clean_resume = preprocess(resume_text)

    clean_job = preprocess(job_description)

    similarity = calculate_similarity(

        clean_resume,

        clean_job

    )

    ats = calculate_ats_score(

        similarity

    )

    keywords = extract_keywords(

        clean_resume

    )

    return {

        "clean_resume": clean_resume,

        "clean_job": clean_job,

        "match": similarity,

        "ats": ats,

        "keywords": keywords

    }