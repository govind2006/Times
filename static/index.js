var myVar = setInterval(myTimer, 1000);
function myTimer() {
  var d = new Date();
  var n = d.toLocaleString();
  document.getElementById("demo").innerHTML = n;
}




  