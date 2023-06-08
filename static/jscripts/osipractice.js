
const person = {
a:0,
b:1,
c:2,
d:3
};

const person2 = {
    0:'a',
    1:'b',
    2:'c',
    3:'d'
};

    

function logChoice(current) {
    // Get the selected radio button
    var selectedOption = document.querySelector('input[name="answer"]:checked');
    var cti = person[selectedOption.value]

    // Log the value of the selected radio button
    if (selectedOption) {
        // console.log(current.className)
        console.log('******************************');
        // console.log('correct to index', cti)
        // console.log(yourmother[bb])
        // console.log('correct answer:', selectedOption.value);
        // console.log('-------------------------');
        // console.log(yourmother[bb]['choices'][cti])
        // console.log('||||||||||||||||||||||||||||||||||||||||||');

    }
  }


function runny(){
    
    var selectedOption = document.querySelector('input[name="answer"]:checked');
    var cti = person[selectedOption.value]
    // console.log('asdasdasd',person[correctAnswer])

    if(selectedOption.className == yourmother[bb]['choices'][cti]){
        document.getElementById('isRight').innerHTML = 'Correct'
        console.log(" Correct");
        //console.log(person2[person[correctAnswer]])
    }
    if(selectedOption.className != yourmother[bb]['choices'][cti]){
        document.getElementById('isRight').innerHTML = 'Wrong'
        console.log("Noooooooooooooooo ")
    }
};