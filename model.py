# Standard Imports
import numpy as np
import pandas as pd
import os
import math
from scipy import stats

# Modeling Imports
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score, precision_score, recall_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier

def model_scores(cm):
    '''
    Function to get all model scores necessary for codeup exercises
    Accepts a confusion matrix, and prints a report with the following:
        Accuracy
        True positive rate
        False positive rate
        True negative rate
        False negative rate 
        Precision
        Recall
        f1-score
        positive support
        negative support
    '''
    
    TN = cm[0,0]
    FP = cm[0,1]
    FN = cm[1,0]
    TP = cm[1,1]
    ALL = TP + FP + FN + TN
    
    print('Model stats:')
   
    # accuracy
    acc = (TP + TN) / ALL
    print('Accuracy: {:.2f}'.format(acc))
    # true positive rate, also recall
    TPR = recall = TP/ (TP + FN)
    print('True Positive Rate: {:.2f}'.format(TPR))
    # false positive rate
    FPR = FP / (FP + TN)
    print('False Positive Rate: {:.2f}'.format(FPR))
    # true negative rate
    TNR = TN / (TN + FP)
    print('True Negative Rate: {:.2f}'.format(TNR))
    # false negative rate
    FNR = FN / (FN + TP)
    print('Flase Negative Rate: {:.2f}'.format(FNR))
    # precision
    precision = TP / (TP + FP)
    print('Precision: {:.2f}'.format(precision))
    # recall
    print('Recall: {:.2f}'.format(recall))
    # f1
    f1_score = 2 * (precision*recall) / (precision+recall)
    print('f1 score: {:.2f}'.format(f1_score))
    # support
    support_pos = TP + FN
    print('Positive support:',support_pos)
    support_neg = FP + TN
    print('Negative support:',support_neg)
    print('-----------------------------------------')

def rf_scores(X_train_telco, y_train_telco, X_validate_telco, y_validate_telco):
    model2 = RandomForestClassifier(min_samples_leaf=12, max_depth=8, random_state=123)
    model2.fit(X_train_telco, y_train_telco)
    y_pred = model2.predict(X_train_telco)
    y_pred_proba = model2.predict_proba(X_train_telco)
    print('RandomForestClassifier min_samples_leaf=12, max_depth=8, random_state=123')
    cm = confusion_matrix(y_train_telco, y_pred)
    model_scores(cm)
    print('Accuracy of random forest classifier on training set: {:.2f}'.format(model2.score(X_train_telco, y_train_telco)))
    print('Accuracy of random forest classifier on validate set: {:.2f}'.format(model2.score(X_validate_telco, y_validate_telco)))

def knn_scores(X_train_telco, y_train_telco, X_validate_telco, y_validate_telco):
    print('KNeighborsClassifier n_neighbors=15')
    model3 = KNeighborsClassifier(n_neighbors=15)
    model3.fit(X_train_telco, y_train_telco)
    y_pred = model3.predict(X_train_telco)
    y_pred_proba = model3.predict_proba(X_train_telco)
    cm = confusion_matrix(y_train_telco, y_pred)
    model_scores(cm)
    print('Accuracy of KNN classifier on training set: {:.2f}'.format(model3.score(X_train_telco, y_train_telco)))
    print('Accuracy of KNN classifier on validate set: {:.2f}'.format(model3.score(X_validate_telco, y_validate_telco)))

def lr_scores(X_train_telco, y_train_telco, X_validate_telco, y_validate_telco):
    print('LogisticRegression C=.01, random_state=123, intercept_scaling=1, solver=lbfgs')
    logit = LogisticRegression(C=.01, random_state=123, intercept_scaling=1, solver='lbfgs')
    logit.fit(X_train_telco, y_train_telco)
    y_pred = logit.predict(X_train_telco)
    y_pred_proba = logit.predict_proba(X_train_telco)
    cm = confusion_matrix(y_train_telco, y_pred)
    model_scores(cm)
    print('Accuracy of Logistic Regression classifier on training set: {:.2f}'.format(logit.score(X_train_telco, y_train_telco)))
    print('Accuracy of Logistic Regression classifier on validate set: {:.2f}'.format(logit.score(X_train_telco, y_train_telco)))