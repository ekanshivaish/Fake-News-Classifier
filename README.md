#  *Nlp-Fake-News-Classifier*
  
- This is a text classifier project based upon news articles data report
- Given are the URLs, heading and Body of news articles along with a target data of Labels.
- Label 1 is called for Real news and vice-versa.
- Used Natural Language processing text cleaning methods such as custom exploring, Lemmatization, stemming and stopword removal to get the useful text out of Body column.
 
# Introduction to NLP method 
- Natural language processing is a subfield of linguistics, computer science, and artificial intelligence concerned with the interactions between computers and human language, in particular how to program computers to process and analyze large amounts of natural language data

# NLP Text cleaning
- Text cleaning is the process of preparing raw text for NLP (Natural Language Processing) so that machines can understand human language.
- Clean text is human language rearranged into a format that machine models can understand. Text cleaning can be performed using simple Python code that eliminates stopwords, removes unicode words, and simplifies complex words to their root form.


## Removing Stopwords
- We are well on our way but still have some words that don’t directly apply to interpretation. Luckily, a number of stopword lists for english and other languages exist and can be easily applied. 


## Custom Exploring
- Punctuation, Emoji’s, URL’s and @’s confuse AI models because they are uniques signatures that either end up being translated unhelpfully into unicode (Smiley face becomes \u200c or similar), or are unique (in the case of @’s and hyperlinks).
- Punctuation also creates noise and impedes NLP understanding because it relates to the tone of the specific sentence, not necessarily the word it is attached to.


## Stemming and Lemmatization
- Stemming and lemmatization via Python is a bit more obtuse than the three previous techniques. 
- It involves breaking down words to their roots and root meanings respectively. By doing so we can better measure intent.
- While both techniques are similar, they produce different results so it is important to determine the proper one for the analysis you hope to perform.
- Stemming, the simpler of the two, groups words by their root stem. 
- This allows us to recognize that ‘jumping’ ‘jumps’ and ‘jumped’ are all rooted to the same verb (jump) and thus are referring to similar problems.
- Lemmatization, on the other hand, groups words based on root definition, and allows us to differentiate between present, past, and indefinite.
- So, ‘jumps’ and ‘jump’ are grouped into the present ‘jump’, as different from all uses of ‘jumped’ which are grouped together as past tense, and all instances of ‘jumping’ which are grouped together as the indefinite (meaning continuing/continuous).


## WordCloud
- A word cloud (also known as a tag cloud) is a visual representation of words. 
- Cloud creators are used to highlight popular words and phrases based on frequency and relevance. 
- They provide you with quick and simple visual insights that can lead to more in-depth analyses.


## ML methods Used 
- Decision Tree Classifier
- Logistic regression
- Naive Bayes Approach

## Vectorization Methods Used
- CountVectorizer
- Tfidf Vectorizer
