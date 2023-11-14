const menu = document.getElementById("_desktop_top_menu")
const sticky = menu.offsetTop;
var lastScrollTop = 10;

// element should be replaced with the actual target element on which you have applied scroll, use window in case of no target element.
element.addEventListener("scroll", function(){
    if(window.scrollY > sticky){
        menu.classList.add('sticky');
    }else{
        menu.classList.remove('sticky');
    }
   var st = window.scrollY || document.documentElement.scrollTop; // Credits: "https://github.com/qeremy/so/blob/master/so.dom.js#L426"
   if (st > lastScrollTop) {
      menu.style.top = "60px";
   } else if (st < lastScrollTop) {
        menu.style.top = "0px";
   } // else was horizontal scroll
   lastScrollTop = st <= 0 ? 0 : st; // For Mobile or negative scrolling
}, false);