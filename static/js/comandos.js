// document.getElementById('buscar').addEventListener('keyup', buscar);
document.getElementById('home').addEventListener('click', home);


// botones de PC y NINTENDO no estan habilitados ya que no puse CARDS para ellos
// document.getElementById('checkmarkPC').addEventListener('click', pc);
// document.getElementById('checkmarkNINTENDO').addEventListener('click', nintendo);

// funcion buscar busca el texto del input, revisa todas las "cards" 
// y si en el texto NO esta lo que buscamos cambia display a none, si no nada


function showall(){
    var x = document.getElementsByClassName("coman");{
        x.style.display = "block";
  }
}

// function buscar(){
    
//     let elements = document.getElementsByClassName("coman");
//     for(let i = 0; i < elements.length; i++){
//             elements[i].style.display = "block"
//     }

//     let busqueda = document.getElementById('buscar').value.toLowerCase();
//     let elementos = document.getElementsByClassName("text");
//     let divs = document.getElementById("com");
//     console.log(divs)
//     console.log(divs.length)
//     for(let i = 0; i < elements.length; i++){
//         if(!elementos[i].innerText.toLowerCase().includes(busqueda)){
//             divs[i].style.display = 'none';
//         }
//         else{
//             divs[i].style.display = 'block';
//         }
//     }

// }

function home() {

    let elements = document.getElementsByClassName("coman");

    for(let i = 0; i < elements.length; i++){
        if(elements[i].id.includes("homecontent")){
            elements[i].style.display = "block"
        }
        else{
            elements[i].style.display = "none"
        }
    }
  }

function variables() {

let elements = document.getElementsByClassName("coman");

for(let i = 0; i < elements.length; i++){
    if(elements[i].id.includes("variables")){
        elements[i].style.display = "block"
    }
    else{
        elements[i].style.display = "none"
    }
}
}

// function xbox(){
     
//     let elements = document.getElementsByClassName("card");
//     for(let i = 0; i < elements.length; i++){
//         if(elements[i].id.includes("XBOX")){
//             elements[i].classList.toggle('hide')
//         }
//         else{
//             elements[i].classList.toggle('show')
//         }
//     }

// }