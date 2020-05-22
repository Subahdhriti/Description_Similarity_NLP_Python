# Description_Similarity_NLP_Python
Find Similarity of two decsription of materials using TF-IDF and Cosine Similarity
• Approach
 Term Frequency – Inverse Document Frequency(TF-IDF) and Cosine Similarity
 Using ‘TfidfVectorizer’ from ‘sklearn.feature_extraction.text’.
• Algorithm
 Step1: Import dependencies- pandas,numpy,TfidfVectorizer from
 sklearn.feature_extraction.text
 Step2: Import Dataset
 dataset  data.csv
Step3: input  Short description of new item
 Preprocess(input)
Step4: description  an array of strings containing the short description in
 the dataset
Step5: preprocess(descriptions)
Step6: Make Feature Vector of ‘description’
 featureVector = vector.fit_transform(description)
Step7: Make Feature Vector of Input string
 featureVector = vector.fit_transform(input)
Step8: for every short description in dataset
 Pairwise_Cosign_similarity(input, description[i])
 Add similarity to similarity Array
 End for
Step9: maxSim  maximum similarity in similarity array
Step10: if maxSim > 0.5
 Output as Duplicate
 Print(similarity)
 Print(Matched Description)
 If(Still User want to Store)
 Data  input
 End if
 Else
 Output as Unique
 Print(similarity)
 Data  input
 End if
