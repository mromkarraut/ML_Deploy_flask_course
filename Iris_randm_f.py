# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 14:44:34 2019

@author: Omkar R
"""

from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd
 
#loading the dataset
iris=load_iris()
X=iris.data
y=iris.target

#Splitting the data into train and test sets
X_train,X_test,y_train, y_test=train_test_split(X,y,random_state=455)

#Build the model

clf=RandomForestClassifier(n_estimators=20)

#Train the classifier
clf.fit(X_train,y_train)

#predictions
predicted=clf.predict(X_test)

#Check Accuracy
print(accuracy_score(predicted,y_test))

import pickle 

with open('C:/Users/lenovo pc/Desktop/Flask/rf.pkl','wb') as model_pkl:
    pickle.dump(clf,model_pkl)