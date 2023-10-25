let image = document.querySelector(".moon");
let background = document.querySelector(".background");
let darkelements = document.querySelectorAll(".dark");
let maintext = document.querySelectorAll(".maintext");
let checkbox = document.querySelectorAll(".checkbox-item");
let num = 0;
let ultag = document.querySelector(".ultag");
let inputtext = document.querySelector(".inputtext");
let drag = document.querySelector(".drag")

image.addEventListener("click", ()=>{
    if(num==0) {
        document.body.style.backgroundColor="#171823";
        background.style.backgroundImage="url('/newtodo/images/bg-desktop-dark.jpg')";
        image.src="/newtodo/images/icon-sun.svg";
        drag.style.backgroundColor="#171823";
    
        for(let i=0; i<darkelements.length; i++) {
            darkelements[i].classList.add("darkelements");
        }
        for(let z=0; z<maintext.length; z++) {
            maintext[z].style.color="#C8CBE7";
        }
        for(let e=0; e<checkbox.length; e++){
            checkbox[e].style.background="#25273D";
        }
        num=1
    } else {
        document.body.style.backgroundColor="rgba(250,250,250,1)";
        background.style.backgroundImage="url('/newtodo/images/bg-desktop-light.jpg')";
        image.src="/newtodo/images/icon-moon.svg";
        drag.style.backgroundColor="white";
        for(let i=0; i<darkelements.length; i++) {
            darkelements[i].classList.remove("darkelements");
        }
        for(let z=0; z<maintext.length; z++) {
            maintext[z].style.color="#494C6B";
        }
        for(let e=0; e<checkbox.length; e++){
            checkbox[e].style.background="white";
        }
        num=0
    }

})

let arr = [
    {
        text: "Jog around the park 3x1",
        checked: false,
    },
    {
        text: "Jog around the park 3x2",
        checked: false,
    },
    {
        text: "Jog around the park 3x3",
        checked: false,
    },
    {
        text: "Jog around the park 3x4",
        checked: false,
    },
    {
        text: "Jog around the park 3x5",
        checked: false,
    }
]

function todo() {
    for(let g=0; g<arr.length; g++){
        ultag.innerHTML+=`<li>
    <div class="flexcross"> 
    <div class="checkbox-item">
    <input class="checkbox1" type="checkbox">
    <div class="input-div"></div>
    </div>
    <h3 class="maintext">${arr[g].text}</h3>
    </div>  
    <img class="cross" src="./images/icon-cross.svg"/>
    </li>`
}
}

todo();
let cross = document.querySelectorAll(".cross");

function addtodo(){
    ultag.innerHTML+=`<li>
    <div class="flexcross"> 
    <div class="checkbox-item">
    <input class="checkbox1" type="checkbox">
    <div class="input-div"></div>
    </div>
    <h3 class="maintext">${arr[arr.length-1].text}</h3>
    </div>  
    <img class="cross" src="./images/icon-cross.svg"/>
    </li>`
}


inputtext.addEventListener("keyup", (q)=>{
    if(q.key=="Enter" & q.target.value!=="") {
        arr.push({
            text: q.target.value,
            checked: false
        })
        addtodo();
        q.target.value = "";
        cross = document.querySelector(".cross");
        console.log(cross)
        cross = document.querySelectorAll(".cross");
    }
    

})
