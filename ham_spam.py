# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 15:12:22 2018

@author: Lenovo
"""

import pandas as pd


import warnings
warnings.filterwarnings('ignore')

def ham(check_spam_ham):
    data = pd.read_csv("spam_ham.csv",encoding='latin-1')

    
    #Drop column and name change
    
    data = data.rename(columns={"v1":"label", "v2":"text"})
    #Count observations in each label
    data.label.value_counts()
    
    # convert label to a numerical variable
    data['label_num'] = data.label.map({'ham':0, 'spam':1})
    
    from sklearn.model_selection import train_test_split
    X_train,X_test,y_train,y_test = train_test_split(data["text"],data["label"], test_size = 0.2, random_state = 10)
    
    
    from sklearn.feature_extraction.text import CountVectorizer
    vect = CountVectorizer()
    vect.fit(X_train)
    
    #print(vect.get_feature_names()[0:20])
    #print(vect.get_feature_names()[-20:])
    
    
    X_train_df = vect.transform(X_train)
    X_test_df = vect.transform(X_test)
    
    
    
    
    
    ham_words = ''
    spam_words = ''
    spam = data[data.label_num == 1]
    ham = data[data.label_num ==0]
    
            
    import nltk
    
    #nltk.download()
    for val in spam.text:
        text = val.lower()
        tokens = nltk.word_tokenize(text)
        #tokens = [word for word in tokens if word not in stopwords.words('english')]
        for words in tokens:
            spam_words = spam_words + words + ' '
            
    for val in ham.text:
        text = val.lower()
        tokens = nltk.word_tokenize(text)
        for words in tokens:
            ham_words = ham_words + words + ' '
   
    
    #naive bayes
    prediction = dict()
    
    
    from sklearn.naive_bayes import MultinomialNB
    model = MultinomialNB()
    model.fit(X_train_df,y_train)
    
    prediction["Multinomial"] = model.predict(X_test_df)
   
    
    test_str_series = list()
    test_str_series.append(check_spam_ham)
    test_str_df = vect.transform(test_str_series)
    
    predict_result=model.predict(test_str_df)
    
    return predict_result[0]
   













































































