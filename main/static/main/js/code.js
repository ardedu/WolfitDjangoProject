
let open_aside = document.getElementById('open_aside');
let aside = document.getElementById('aside');
let close_aside = document.getElementById('close_aside')
if (open_aside) {
    open_aside.addEventListener("click", () => {
    
    aside.style.display = "block";
    
    aside.style.zIndex = "2";
    aside.style.width = "300px";
    aside.style.marginTop = "0";
    
    close_aside.style.display = 'block';
    close_aside.style.zIndex = "3";
  });
}

if (close_aside) {
  close_aside.addEventListener("click", () => {
  
  aside.style.display = "none";
  
 
});
}




