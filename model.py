import pandas as pd
import numpy as np
import nltk
from sklearn.model_selection import train_test_split
import pickle


df= pd.read_csv("data.csv", sep=',')
df= df.dropna()
df['Text']= df['Headline'] + ' '+ df['Body']
to_drop= ['Headline','Body', 'URLs']
df.drop(to_drop, axis=1,inplace= True)
print(df)


from sklearn.feature_extraction.text import CountVectorizer
cv= CountVectorizer()
with open('cv_vec_02082021.pkl', 'wb') as f:
    pickle.dump(cv,f)

X = cv.fit_transform(df['Text'])
y= df['Label']
from sklearn.linear_model import LogisticRegression
model= LogisticRegression()
model.fit(X, y)
#print(model.score(X, y))
filename= 'final_model_02082021.pkl'
with open(filename, 'wb') as f:
    pickle.dump(model, f)