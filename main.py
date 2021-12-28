import detectAnswerWithML as ml
import questions          as q
label_value_before = "label_1"


def mainFunction(katman,label_value):
    question = getQuestion(katman,label_value_before,label_value)
    if (question == False):
        calculateScore(katman)
        isTryAgain()
    print(question)
    answer = input("What do you do?")
    new_label_value = ml.detectAnswer(katman,answer)
    katman = katman+1
    isDead()
    mainFunction(katman,new_label_value)


def getQuestion(katman,label_value_before,label_value):
    arr = q.questions[katman]
    for x in range(len(arr)):
        if(arr[i]["label"].include(label_value) and arr[i]["labelBefore"].include(label_value_before)):
            return arr[i]["question"]
    return False        

def isDead(label_value):
    arrDeadLabels = ["label_1","label2"]
    if label_value in arrDeadLabels : return True



def calculateScore(label_value,katman):
    
    score  = (katman / 10) * 100
    print("You died, SCORE: " + score)

def isTryAgain():
   inputTryAgain = input("Try again ? If yes enter (Y)") 
   if(inputTryAgain =="Y"):
       restartGame()
   else:
       quit()
     
       
def restartGame():
    katman  = 0
    print("Initial quesiton")
    answer = input("What do you do?")
    label_value = ml.detectAnswer(katman,answer)
    mainFunction(katman,label_value)

restartGame()



