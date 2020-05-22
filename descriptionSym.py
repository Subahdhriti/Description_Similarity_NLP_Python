import pandas as pd
from preprocessing import *
import numpy as np
import csv
#from scipy import spatial
from sklearn.feature_extraction.text import TfidfVectorizer



dataset = pd.read_csv('data.csv')
description = dataset.iloc[:,1].values
description = preprocessData(description) 

input= input('Enter Short Description:\n')
input=preprocessInput(input)                 #Preprocessing of Data

#print(input)

#input=[input]
description=np.append(description,input)

vect = TfidfVectorizer(min_df=1, stop_words="english")

                                              #Using TF-IDF
tfidf = vect.fit_transform(description)       #Converting the Description to feature Vector
pairwise_similarity = tfidf * tfidf.T         #Cosine Similarity 
sim=pairwise_similarity.toarray()

sim2=sim[len(sim)-1]
max=0
for i in range(0,len(sim2)-1):
    if sim2[i]>max:
        max=sim2[i]
        loc=i
if max>0.5:
    print('THE MATERIAL IS ALREADY PRESENT \n')
    print('Similarity: ' ,max )
    print('Matched Description:\n',description[loc])
else:
    print('THE MATERIAL IS UNIQUE \n')
    print('Similarity: ' ,max )
    row=[len(description)-1,input]
    with open('data.csv', 'a+', newline='\n') as write_obj:
            writer=csv.writer(write_obj)
            writer.writerow(row)
            print('Store successfull')

#words = input.split()
#print(words[0])
#vector1=gensim.models.Word2Vec(words, min_count = 1,size = 100, window = 5)

#vector2=gensim.models.Word2Vec(words, min_count = 1,size = 100, window = 5)

#vector1= featureVector(input,num_features=300)

#similarity = 1 - spatial.distance.cosine(vector1, vector2)

#def findDuplicates(input):


    