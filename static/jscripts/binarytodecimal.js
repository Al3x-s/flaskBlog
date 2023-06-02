
function checkAnswer(current, num, classname){
    var parentClass = current.parentNode.parentNode.className;
    var correctAnswer =  test3[num];
    var userguess = classname;
    console.log(userguess)
    if(correctAnswer == userguess){
        console.log("answer is right")
        document.querySelector("." + parentClass).classList.remove('table-danger')
        document.querySelector("." + parentClass).classList.add('table-success')
    }
    else if(correctAnswer != userguess){
        console.log("wrong")
        document.querySelector("." + parentClass).classList.remove('table-success')
        document.querySelector("." + parentClass).classList.add('table-danger')
    }
}
