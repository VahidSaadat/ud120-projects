#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###

# clf = SVC(kernel='linear')
clf = SVC(C=10000 , kernel='rbf')   # accuracy: 0.99

#features_train = features_train[:len(features_train)/100]
#labels_train = labels_train[:len(labels_train)/100]
train_time = time()
clf.fit(features_train, labels_train)
print "training time:", round(time()-train_time, 3), "s"

pred_time = time()
pred = clf.predict(features_test)
print "prediction time:", round(time()-pred_time, 3), "s"

pred = clf.predict(features_test)
print "accuracy score:", accuracy_score(labels_test, pred)

print "pred[10]:", pred[10]    #1
print "pred[26]:", pred[26]    #0
print "pred[50]:", pred[50]    #1

Chris_counter = 0
for pred_labels in pred:
    if pred_labels == 1:
        Chris_counter += 1
print Chris_counter     #877

#########################################################


