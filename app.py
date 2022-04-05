import pandas as pd
import numpy as np
import streamlit as st
import nltk
import regex as re
import sklearn
import pickle
from nltk import WordNetLemmatizer
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
lm = WordNetLemmatizer()
sw = stopwords.words('english')

model = pd.read_pickle(r'C:\Users\HP\PycharmProjects\pythonProject\final_model.pickle')
vect = pd.read_pickle(r'C:\Users\HP\PycharmProjects\pythonProject\vec_new.pickle')


def clean_data(value):
    value = value.lower()
    value = re.sub(r'[^\w\s]', '', value)
    value = re.sub(r'[^a-zA-Z]', ' ', value)
    value = re.sub('aa[a]*', 'a', value)
    value = re.sub(r"http\S+", "", value)
    value = re.sub(r'\<a href', ' ', value)
    value = re.sub(r'[_"\;%()|+&=*%.,!?:#$@\[\]/]', ' ', value)
    value = re.sub('-', ' ', value)
    value = re.sub('\d+', '', value)
    value = re.sub('\s\s+', ' ', value)
    value = re.sub('\n', '', value)
    value = re.sub('<[^>]*>', '', value)
    return value


cv = CountVectorizer()


def predict(a):
    cd = clean_data(a)
    print(cd)     #  to check output of clean_data function
    data = vect.transform([cd])
    print(data)   #  #  to check output of clean_data function
    prediction = model.predict(cd)
    return prediction


def main():
    st.title("""
    **NEWS CLASSIFIER APP**
    """)

    html_temp = """
    <div style= "background-color:#825246; padding:10px>
    <h2 style = "color: white; text-align:center ;">Fake News detector ML app</h2>
    </div>
    """

    st.markdown(html_temp, unsafe_allow_html=True)
    st.subheader("Enter the news article you are not sure about")
    user_input = st.text_input("Your news here below", "#SAMPLE TEXT#")

    st.subheader("cleaned and preprocessed data")
    st.write(clean_data(user_input))
    if st.button("classify"):
        output = predict(user_input)
        if output == 0:
            st.success('The above news is Fake')
        else:
            st.success('This is a real news')

    else:
        st.write("No input")


if __name__ == '__main__':
    main()
