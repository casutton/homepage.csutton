/* Code for showing and hiding the bibtex and abstract on user clicks */

var ie4 = false; if(document.all) { ie4 = true; }
function getObj(id) { if (ie4) { return document.all[id]; } else { return document.getElementById(id); } }

function toggle(elemName, linkName, text) {
           elem = getObj (elemName);
           link = getObj (linkName);
           if (elem.style.display == 'block') {
              elem.style.display = 'none';
              link.innerHTML = text;
           } else {
              elem.style.display = 'block';
              link.innerHTML = 'hide '+text;
           }     
}
