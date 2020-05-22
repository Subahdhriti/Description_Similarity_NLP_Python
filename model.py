import gensim 
from gensim.models import Word2Vec 
import numpy as np
from gensim.models import KeyedVectors

def featureVector(input,num_features):
    words = input.split()
    featureVec = np.zeros((num_features,), dtype='float32')
    num_words = 0
    for word in words:
        num_words += 1
        featureVec = np.add(featureVec, gensim.models.Word2Vec(word, min_count = 1,size = 100, window = 5))

    if (num_words > 0):
        featureVec = np.divide(featureVec, num_words)

    return featureVec

print("[INFO] Model loaded...")
