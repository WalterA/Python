const express = require('express');
const cors = require('cors')
const app = express();

// app.use(cors());

// var iPortaTcp = 4201;
// var sIpAddress = "172.22.228.243"

// app.listen(iPortaTcp,sIpAddress, () => console.log('API is running on http://' + sIpAddress + ':' + iPortaTcp));
// const bodyParser = require('body-parser');
// app.use(bodyParser.urlencoded({ extended: true }));

// //PRIMA ROUTE
// app.get('', (req, res) => {
//     console.log("Mi hai chiesto la pagina iniziale");
//     res.sendFile("index.html", { root: './htdocs' });
//     });
// // SECONDA ROUTE
// app.get('/registrati.html', (req, res) => {
//     console.log("Mi hai chiesto la pagina registrazione");
//     res.sendFile("registrati.html", { root: './htdocs' });
//     });
// //TERZA ROUTE
// app.get('/accedi.html', (req, res) => {
//     console.log("Mi hai chiesto la pagina accesso");
//     res.sendFile("accedi.html", { root: './htdocs' });
//     });

// app.get('/style.css', (req, res) => {
//     console.log("Mi hai chiesto la pagina css");
//     res.sendFile("style.css", { root: './htdocs' });
//     });
// app.get('/gestisciDatiForm', (req, res) => {
//     console.log("Mi hai chiesto la pagina dati");
//     res.send("<html><body>ciao " + req.query.username +"</body></html>");
//     });



var A;
var B;
A = 3;
B = "buongiorno a tutti";
console.log("Il tipo della var A e' " + typeof(A) + "\n");
console.log("Il tipo della var B e' " + typeof (B) + "\n");

