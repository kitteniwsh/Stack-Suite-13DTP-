
console.log('strfing');
function onLoad() {
  document.getElementById("Encrypt").style.display = "none";
  document.getElementById("Decrypt").style.display = "none";
  document.getElementById("Totient").style.display = "none";
  document.getElementById("PEM").style.display = "none";
  document.getElementById("automatic").style.display = "none";
  var pss = sessionStorage.getItem("pastselection");
  var status = document.getElementById("menuHandler");
  status.value = pss;
  if(pss == null){
    status.value = "Encrypt";
  }
  document.getElementById(status.value).style.display = "";
}

window.onload = onLoad;
function cS(){
  var status = document.getElementById("menuHandler");
  document.getElementById("Encrypt").style.display = "none";
  document.getElementById("Decrypt").style.display = "none";
  document.getElementById("Totient").style.display = "none";
  document.getElementById("PEM").style.display = "none";
  document.getElementById("automatic").style.display = "none";


 document.getElementById(status.value).style.display = "";
 sessionStorage.setItem("pastselection", status.value);


}
