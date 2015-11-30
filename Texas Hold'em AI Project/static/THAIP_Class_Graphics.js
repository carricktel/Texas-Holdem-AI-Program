

function init() {
  if (event.keyCode == 13){
	newtext = document.getElementById("userinput")
	newtext.disabled = true;
    oldtext = document.getElementById("interface");
    oldtext.value = oldtext.value + "\n" + newtext.value;
    newtext.value = "";    
	newtext.disabled = false;
	newtext.focus();
	newtext.select();
    }

}
