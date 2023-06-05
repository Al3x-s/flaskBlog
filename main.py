from flask import Flask, render_template, request, session
from flask import g
import random
from functions import *
from questions import *



##----------------------------------------------------##

app = Flask(__name__)
key = str(random.randint(-7,999999))
app.secret_key = key

@app.before_request
def before_request():
    session.modified = False


@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/index.html")
def despHome():
    return render_template('index.html')

@app.route("/binarytodecimal.html")
def BinToDec():
    ##----------------------------------------------------##
    BinaryList = []
    binaryCorrectAnswers = []
    classlist = []
    ####################################################
    for i in range(10):
        BinaryList.append(createRandomBinary())
    ####################################################
    for i in BinaryList:
        binaryCorrectAnswers.append(binaryToDecimal(i))
    ####################################################
    for i in range(1,11):
        classlist.append(("guess"+str(i)))
    ##----------------------------------------------------##
    return render_template('binarytodecimal.html', blist=BinaryList, alist=binaryCorrectAnswers, clist=classlist)


@app.route("/decimaltobinary.html")
def dectobin():
    binlist = []
    aList=[]
    for i in range(10):
        binlist.append(createRandomDecimal())
    print(binlist)
    for i in binlist:
        aList.append(fixBinary(DecimalToBinary(i)))
    
    return(render_template("decimaltobinary.html", alist=aList, binlist=binlist))


@app.route("/classguess.html")
def calssguess():
    ##----------------------------------------------------##    
    classes = ['A', 'B','C', 'D', 'E']
    ipclasses = []
    divClassName = []
    ####################################################
    for i in range(10):
        ipclasses.append(random.choice(classes))
    ####################################################
    for i in range(1,11):
        divClassName.append(("guess"+str(i)))
    ####################################################
    x = generate_random_ip_address(ipclasses)    
    return(render_template('classguess.html', iplist=x, iclasses=ipclasses, dClassName=divClassName))

@app.route("/bitwise.html")
def bitwise():
    ##----------------------------------------------------##    
    listofdic = []
    divClassNames = []
    for i in range(1,11):
        divClassNames.append(str(i))
    ####################################################
    for i in range(10):
        yy = calculate_network_info()
        listofdic.append(yy)
    return render_template('bitwise.html', listOfDictionaries=listofdic, clist=divClassNames)

@app.route("/osipractice.html", methods=["GET", "POST"])
def osi():
    score = session.get("score", 0)
    session["score"] = 0
    question_number = random.randint(1,50)
    question = osiQuestions.get(question_number)
    lastq = session.get("lastq", False)
    
    if request.method == 'POST':
        user_answer = request.form.get('answer')
        # Check if the user's answer is correct
        if user_answer == question['answer']:
            # Move to the next question
            question = osiQuestions.get(question_number)
            score += 1
            lastq = True
            print("yeeeees")
        if user_answer != question['answer']:
            question = osiQuestions.get(question_number)
            print("nooooooooooooooo")
            lastq = False
    if lastq:
        lastq = 'Correct'
    if not lastq:
        lastq=''
    session["score"] = score
    session["lastq"] = lastq
    
            
    return(render_template('osipractice.html', osiQuestions=osiQuestions, question=question, nor=score, qn=question_number, lastq=lastq))

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)