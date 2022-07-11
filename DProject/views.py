from django.http import HttpResponse
from django.shortcuts import render
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics


def home(request):
    return render(request, "home.html")

def predict(request):
    return render(request, "prediction.html")

def result(request):
    val1 = float(request.GET['n1'])
    val2 = float(request.GET['n2'])
    val3 = float(request.GET['n3'])
    val4 = float(request.GET['n4'])
    val5 = float(request.GET['n5'])
    val6 = float(request.GET['n6'])
    val7 = float(request.GET['n7'])
    val8 = float(request.GET['n8'])


    #Loading dataset
    diabetes = pd.read_csv('C:/Users/dell/diabetes.csv')

    #Train test split
    logmodel = LogisticRegression()
    X_train, X_test, y_train, y_test = train_test_split(diabetes.drop('Outcome', axis=1), diabetes['Outcome'], test_size=0.30)
    logmodel.fit(X_train, y_train)
    pred = logmodel.predict([[val1, val2, val3, val4, val5, val6, val7, val8]])
    res = ""
    if pred == [1]:
        res = "Positive"
    else:
        res = "Negative"

    return render(request, "prediction.html", {"result2": res})
