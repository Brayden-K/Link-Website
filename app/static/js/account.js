function updateBtnWidth(newVal){
    document.getElementById("buttonwidthlabel").textContent="Button Width " + newVal + "%";
    document.getElementById("examplebtn").style.width = newVal + '%';
}

function updateBtnRadius(newVal){
    document.getElementById("buttonradiuslabel").textContent="Button Radius " + newVal + "px";
    document.getElementById("examplebtn").style.borderRadius = newVal + 'px';
}

function updateBtnColor(newVal){
    document.getElementById("examplebtn").style.backgroundColor = newVal;
}

function updateNameColor(newVal){
    document.getElementById("username").style.color = newVal;
}

function updateBtnBackgroundHover(newVal){
    const old = document.getElementById("examplebtn").style.backgroundColor
    document.getElementById("examplebtn").onmouseover = function() 
    {
        this.style.backgroundColor = newVal;
    }
    document.getElementById("examplebtn").onmouseleave = function() 
    {
        this.style.backgroundColor = old;
    }
}

function updateBtnTextColor(newVal){
    document.getElementById("examplebtn").style.color = newVal;
}

function updateBtnBorderColor(newVal){
    document.getElementById("examplebtn").style.borderColor = newVal;
}

function updateBackgroundColor(){
    const firstColor = document.getElementById("backgroundcolor1").value
    const secondColor = document.getElementById('backgroundcolor2').value
    const radius = document.getElementById('bgradius').value
    document.getElementById("bgradiuslabel").textContent="Background Radius " + radius + "°";
    document.getElementById("examplecontainer").style.background = 'linear-gradient('+ radius +'deg, '+ firstColor +' 0%, '+ secondColor +' 100%)';
}