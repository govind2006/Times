var myVar = setInterval(myTimer, 1000);
function myTimer() {
  var d = new Date();
  var n = d.toLocaleString();
  document.getElementById("demo").innerHTML = n;
}

function myFunction() {
    document.getElementById("myDropdown").classList.toggle("show");
  }
  
 window.onclick = function(event) {
    if (!event.target.matches('.dropbtn')) {
      var dropdowns = document.getElementsByClassName("dropdown-content");
      var i;
      for (i = 0; i < dropdowns.length; i++) {
        var openDropdown = dropdowns[i];
        if (openDropdown.classList.contains('show')) {
          openDropdown.classList.remove('show');
        }
      }
    }
  }


  