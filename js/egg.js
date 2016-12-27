function do_switch () {
   mode = (mode + 1) % 3;
   if (mode == 0) {
     switch_to_std_cas ()	
  } else if (mode == 1) {
     switch_to_red_cas ()
  } else if (mode == 2) {
     switch_to_bw_cas ()	
   }
 }


  function setActiveStyleSheet(title) {
     var i, a, main;
     for(i=0; (a = document.getElementsByTagName("link")[i]); i++) {
       if(a.getAttribute("rel").indexOf("style") != -1
          && a.getAttribute("title")) {
         a.disabled = true;
         if(a.getAttribute("title") == title) a.disabled = false;
       }
     } 
  }


 function switch_to_red_cas () {
   document.magic_photo.src = 'images/charles.jpg'	
   setActiveStyleSheet ("red")
   egg = document.getElementById ("egg")
   egg.innerHTML = "You found the Easter egg! Now try clicking my photo again."
 }

 function switch_to_std_cas  () {
   document.magic_photo.src = 'images/charles3.jpg'	
   setActiveStyleSheet ("standard")
  egg = document.getElementById ("egg")
   egg.innerHTML = "Had enough of silliness? You turned off the Easter egg."
 }

 function switch_to_bw_cas () {
   document.magic_photo.src = 'images/charles-bw.jpg'	
   setActiveStyleSheet ("bw")
   egg = document.getElementById ("egg")
   egg.innerHTML = "Don't much like colour, do you?"
 }

 mode = 0
