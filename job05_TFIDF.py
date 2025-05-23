import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from scipy.io import mmwrite, mmread

df_reviews = pd.read_csv('./cleaned_data/cleaned_reviews.csv')
df_reviews.dropna(inplace=True)
df_reviews.info()

tfidf = TfidfVectorizer(sublinear_tf=True)
tfidf_matrix = tfidf.fit_transform(df_reviews['reviews'])
print(tfidf_matrix.shape)
print(tfidf_matrix[0])

import pickle

with open('./models/tfidf.pickle', 'wb') as f:
    pickle.dump(tfidf, f)

mmwrite('./models/tfidf_movie_review.mtx', tfidf_matrix) # 매트릭스로써 저장