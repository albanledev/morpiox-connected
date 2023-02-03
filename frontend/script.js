//on charge les informations utiles

const statut = document.querySelector("h2");
let jeuActif = true;

let etatJeu = ["","","",
               "","","",
               "","",""]

let joueurActif = "X"

//victoires





// messages 



const gagne = () => {
    return `Le joueur ${joueurActif} a gagné la partie !`
}

const egalite = () => {
     return `Egalité, recommencer la partie`
}

const tourJoueur = () => {
     return `C'est au tour du joueur ${joueurActif} de jouer`
}

statut.innerHTML = tourJoueur();

// conditions de victoire


//document.querySelectorAll(".case").forEach(cell => cell.addEventListener("click",gestionClickCase))

// document.querySelector(".recommencer").addEventListener("click", recommencer);

const conditionsVictoire = 
    [
    [0,1,2],
    [3,4,5],
    [6,7,8],
    [0,3,6],
    [1,4,7],
    [2,5,8],
    [0,4,8],
    [2,4,6]
    
]


function gestionClickCase() {
    // console.log(this)
    const indexCase = parseInt(this.dataset.index)
    // console.log(indexCase)

    if (etatJeu[indexCase] != "" || jeuActif != true){
        return
    }

    etatJeu[indexCase] = joueurActif
    if(joueurActif=="X"){

            this.style.color="blue"

    }else {
        this.style.color="red"
    }
    this.innerHTML = joueurActif
    console.log(etatJeu)
    console.log(joueurActif)

    verifGagne()

    // joueurActif. = "O"




}

function verifGagne(){
    let tourGagnant = false 
    for (let conditionVictoire of conditionsVictoire){
        let val1 = etatJeu[conditionVictoire[0]]
        let val2 = etatJeu[conditionVictoire[1]]
        let val3 = etatJeu[conditionVictoire[2]]
        if (val1 == "" || val2 == "" ||val3 == ""){
            continue
        }
        if (val1 == val2 && val2 ==val3){
            tourGagnant=true
            break 
        }
    }

    if(tourGagnant){
        statut.innerHTML = `Le joueur ${joueurActif} a gagné !`
        jeuActif = false
        return 
    }

    if (!etatJeu.includes("")){
        statut.innerHTML = egalite(); 
        jeuActif = false
        return
    }
 
    if (joueurActif == "X"){
        joueurActif="O"
        // this.style.color = "red"
        // joueurActif.style.color = "green"
        //document.querySelector()
    }else {
        joueurActif="X"
        
    }
    statut.innerHTML = `Au tour du joueur ${joueurActif}`
}




let recommencer = document.querySelector('#recommencer')
recommencer.addEventListener('click', () => {
     etatJeu = ["","","",
    "","","",
    "","",""],
     jeuActif = true;
     joueurActif = "X"

})

// const recommencer = () => {

// }

// const button = document.querySelector("#button")
const listButton = document.querySelectorAll(".case")
listButton.forEach(e =>{
    e.addEventListener("click",gestionClickCase)
    e.addEventListener("click", () => {
        fetch("http://192.168.43.19:3000", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                 "data" : etatJeu,
                 "joueur" : joueurActif,
                 "jeu" : jeuActif

            })
        })
            .then(res => res.json())
            .then(data => {
                console.log(data)
            })
    })
})