from flask import Flask, render_template
from functions import *



##----------------------------------------------------##

app = Flask(__name__)

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



@app.route("/classguess.html")
def calssguess():
    ##----------------------------------------------------##    
    classes = ['A', 'B','C','D', 'E' ]
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

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)