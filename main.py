from flask import Flask, render_template
from functions import *



##----------------------------------------------------##

app = Flask(__name__)

@app.route("/")
def hello_world():
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