#! /usr/bin/env python
# -*- coding: UTF-8 -*-
import detectAnswerWithML as ml
import questions          as q
"""
import sys
import os
from PyQt6.QtGui import QGuiApplication
from PyQt6.QtQml import QQmlApplicationEngine
from PyQt6.QtQuick import QQuickWindow

QQuickWindow.setSceneGraphBackend('software')
app = QGuiApplication(sys.argv)
engine = QQmlApplicationEngine()
engine.quit.connect(app.quit)
engine.load('./main.qml')
sys.exit(app.exec())
"""

def getQuestion(katman,label_value_before,label_value):
    arr = q.questions[katman]
    for x in range(len(arr)):
        if(arr[x]["label"] in label_value and label_value_before in arr[x]["labelBefore"]):
             return arr[x]["question"]
    print("Yanlis Yanıt Girdiniz")
    restartGame()
    

def mainFunction(katman,label_value,label_value_before):
    question = getQuestion(katman,label_value_before,label_value)
    katman = katman+1
    print(chr(27) + "[2J")
    print(question)
    isDead(label_value,katman)
    answer = input(" Ne yaparsın? ")
    new_label_value = ml.detectAnswer(katman,answer)
    new_label_value_before = label_value
    mainFunction(katman,new_label_value,new_label_value_before)

def restartGame():
    katman  = 0
    print("Bindiğin gemi battı ve kendini bilmediğin bir adanın kumsalında buldun neler olduğunu zar zor hatırlıyorsun. Hava soğuk gökyüzüne baktığında kara kara bulutların olduğunu görüyorsun. Sığınacak bir yer bulma umuduyla etrafına baktığında biraz ötede bir mağara görüyorsun bir de büyük ağaçların olduğu orman ")
    answer = input(" Ne yaparsın? ")
    label_value = ml.detectAnswer(katman,answer)
    label_value_before = "1"
    mainFunction(katman,label_value,label_value_before)




def isDead(label_value,katman):
    arrDeadLabels = ["7","11","13","16","24","25","29","33","35","37"]
    arrWinLabels =  ["36"]
    if label_value in arrDeadLabels: calculateScore("öldünüz",katman)
    if label_value in arrWinLabels:  calculateScore("kazandınız",katman)
    return 


def isTryAgain():
   inputTryAgain = input("Tekrar oynamak isterseniz (y) basın ") 
   if(inputTryAgain =="y"):
       restartGame()
   else:
       quit()

def calculateScore(message , katman):
    
    score  = ((katman+1) / 10) * 100
    print(message + " SCORE: " + str(score))
    isTryAgain()



restartGame()
       
 


