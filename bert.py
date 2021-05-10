import pandas as pd
import numpy as np
import json
import wikipedia
import json

df = pd.read_csv('Final.csv')
pub_df = df.drop(['Unnamed: 0'], axis=1)
pub_df

import ast
interest = []

for i in range(12528):
  stringA = pub_df['Research Interests'][i]
  res = ast.literal_eval(stringA)
  interest += res
interest = list(set(interest))


from scipy import spatial
from sent2vec.vectorizer import Vectorizer


vectorizer = Vectorizer()
vectorizer.bert(interest)
vectors_bert = vectorizer.vectors

dist_1 = spatial.distance.cosine(vectors_bert[0], vectors_bert[1])
dist_2 = spatial.distance.cosine(vectors_bert[0], vectors_bert[2])
print('dist_1: {0}, dist_2: {1}'.format(dist_1, dist_2))
# dist_1: 0.043, dist_2: 0.192

