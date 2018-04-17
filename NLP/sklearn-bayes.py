#coding=utf-8
#load news data
from sklearn.datasets import fetch_20newsgroups
from sklearn.cross_validation import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report

news=fetch_20newsgroups(subset='all')
print(len(news.data))
print(news.data[0])
#-------------split data
#75% training set,25% testing set
X_train,X_test,y_train,y_test=train_test_split(news.data,news.target,test_size=0.25,random_state=33)
#-------------transfer data to vector
vec=CountVectorizer()
X_train=vec.fit_transform(X_train)
vectorizer_test = CountVectorizer(vocabulary=vec.vocabulary_)
X_test = vectorizer_test.transform(X_test)
#-------------training
#initialize NB model with default config
mnb=MultinomialNB()
#training model
mnb.fit(X_train,y_train)
#run on test data
y_predict=mnb.predict(X_test)
#-------------performance
print('The Accuracy is',mnb.score(X_test,y_test))
print(classification_report(y_test,y_predict,target_names=news.target_names))
