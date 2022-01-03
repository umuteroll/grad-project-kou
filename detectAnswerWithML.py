import pandas as pd 
from   pandas import DataFrame as df
import numpy as np
import fasttext 


def isResultValid(result,katman):
    if(float(result[1])<0.88):
        print("Alakasız bir yanıt girdininiz")
        answer2 = input("Lütfen Tekrar bir yanıt girin")
        detectAnswer(katman,answer2)
    return result[0][0][9:]

def detectAnswer(katman,answer):
  fileName = "model"+str(katman)+".csv"
  model = fasttext.train_supervised(input=fileName, epoch=200, lr=0.8, wordNgrams=1,loss='hs',dim=300)
  result = model.predict(answer,k=1)
  return isResultValid(result,katman)

