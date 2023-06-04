function checkAnswer(current, num, usg,ung,ubs,uhg){
    var parentClass = current.parentNode.parentNode.className;
    var correctSubnetAnswer =  t1[num]['subnetMask'];
    var correctNetworkAnswer =  t1[num]['networkAddress'];
    var correctBroadcastAnswer =  t1[num]['broadcastAddress'];
    var correctHostAnswer =  t1[num]['totalhosts'];
    /////////////////////////////////////////////
    var userSubnetGuess = usg;
    var userNetworkGuess = ung;
    var userBroadcastGuess = ubs;
    var userHostGuess = uhg;
    

    if(userSubnetGuess == correctSubnetAnswer && userNetworkGuess == correctNetworkAnswer && userBroadcastGuess == correctBroadcastAnswer && userHostGuess == correctHostAnswer){
        console.log("yes")
        document.querySelector("." + parentClass).style.backgroundColor = "#0F9D58"
    }
    else if(userSubnetGuess != correctSubnetAnswer && userNetworkGuess != correctNetworkAnswer && userBroadcastGuess != correctBroadcastAnswer && userHostGuess != correctHostAnswer){
        console.log("wrong")
        document.querySelector("." + parentClass).style.backgroundColor = "#de5246"
    }
}

fetch('https://steamcommunity.com/market/pricehistory/?appid=730&market_hash_name=MP9%20%7C%20Rose%20Iron%20(Minimal%20Wear)')
  .then(response => response.json())
  .then(data => {
    if (data && data.length > 0) {
      const firstItem = data[0];
      console.log(firstItem);
    } else {
      console.log('No JSON data received.');
    }
  })
  .catch(error => {
    console.log('Error occurred:', error);
  });
