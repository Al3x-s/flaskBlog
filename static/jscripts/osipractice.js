
x = 0;
function logChoice() {
    // Get the selected radio button
    var selectedOption = document.querySelector('input[name="answer"]:checked');
    
    // Log the value of the selected radio button
    if (selectedOption) {
        x = x +1; 
        console.log(x)
        console.log('Selected choice:', selectedOption.value);
    }
  }

function run(br){
    console.log("br")
}