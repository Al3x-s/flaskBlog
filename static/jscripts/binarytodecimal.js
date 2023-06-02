
function checkAnswer(current, num, classname){
    var parentClass = current.parentNode.parentNode.className;
    var correctAnswer =  test3[num];
    var userguess = classname;
    console.log(userguess)
    if(correctAnswer == userguess){
        console.log("answer is right")
        document.querySelector("." + parentClass).style.backgroundColor = "#0F9D58"
    }
    else if(correctAnswer != userguess){
        console.log("wrong")
        document.querySelector("." + parentClass).style.backgroundColor = "#de5246"
    }
}