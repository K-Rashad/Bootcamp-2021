
var btn = document.getElementsByClassName("faq-btn");
var i;

for (i = 0; i < btn.length; i++) {
    btn[i].addEventListener("click", function () {
        this.classList.toggle("active");
        var p = this.nextElementSibling;
        if (p.style.maxHeight) {
            p.style.maxHeight = null;
        } else {
            p.style.maxHeight = p.scrollHeight + "px";
        }
    });
}
