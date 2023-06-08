
function checkAnswer(current, num, classname){
    var parentClass = current.parentNode.parentNode.className;
    var correctAnswer =  test3[num];
    var userguess = classname;
    parentClass = parentClass.substring(0,5);
    if(correctAnswer == userguess){
        document.querySelector("." + parentClass).style.backgroundColor = "#0F9D58"
     
    }
    else if(correctAnswer != userguess){
        document.querySelector("." + parentClass).style.backgroundColor = "#de5246"
    }
}