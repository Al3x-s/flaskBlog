
function checkAnswer(current, num, classname){
    var parentClass = current.parentNode.parentNode.className;
    var correctAnswer =  yourmom[num];
    var userguess = classname;
    console.log(userguess)
    if(correctAnswer == userguess.toUpperCase()){
        document.querySelector("." + parentClass).style.backgroundColor = "#0F9D58"
    }
    else if(correctAnswer != userguess.toUpperCase()){
        document.querySelector("." + parentClass).style.backgroundColor = "#de5246"
    }
}