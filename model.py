import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
df = pd.read_csv('dataset/movies.csv')

# Handle missing values
df['genre'] = df['genre'].fillna('')

# Convert text → numbers
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(df['genre'])

# Similarity matrix
similarity = cosine_similarity(tfidf_matrix)

# Get all movie titles
def get_all_titles():
    return df['title'].tolist()

# Recommend movies
def recommend_movies(movie_name):
    if movie_name not in df['title'].values:
        return ["Movie not found"]

    index = df[df['title'] == movie_name].index[0]

    scores = list(enumerate(similarity[index]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)

    recommended = []
    for i in scores[1:6]:
        recommended.append(df.iloc[i[0]]['title'])

    return recommended