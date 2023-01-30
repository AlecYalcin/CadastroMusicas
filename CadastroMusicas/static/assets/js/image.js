imageLink = document.querySelector("#mu_capa")
srcCapa   = document.querySelector("#srcCapa")

imageLink.onchange = function() {
    srcCapa.src = imageLink.value
}