const express = require("express")
const app = express()
const http = require("http")
const ip = require("ip")
// const {console} = require("console")
// const io = require('socket.io')
// console.log(io.Server)
console.log(ip.address())

let etatJeu = ["","","",
               "","","",
               "","",""]

let joueurActif = "X"      

let jeuActif = true

const cors = require("cors")

const port = 3000
console.log("ouiii")
const server = http.createServer(app)

app.use(cors())
// express.json()
app.use(express.json())

app.get('/', (req, res) => {
    res.send({
    "data": etatJeu,
    "joueur": joueurActif,
    "jeu": jeuActif
    });
    });

app.post('/', (req,res) => {
    // console.log(req.query.year)
    // console.log(req.body.joueur)
    etatJeu = req.body.data
    joueurActif = req.body.joueur
    jeuActif = req.body.jeu


    res.send({"msg":"ok",
              "joueur":req.body.joueur,
              "jeu":req.body.jeu
})
    // res.json()
})          


server.listen(port,() => {
    console.log(`On écoute sur le port ${port} `)
})
