
function capitalizeFirstLetter(string) {
    return string.charAt(0).toUpperCase() + string.slice(1);
}



console.log("ciao");

// const str = prompt('Enter a string:');
// console.log("Hai inserito " + capitalizeFirstLetter(str));
// process.exit(0);

function VerificaNumero(sNum) 
{
    for(i=0;i<sNum.length;i++)
    {
        if ((sNum.charAt(i)<'0') || (sNum.charAt(i)>'9'))
            return false;
    }
    return true
}

function parseIntmy(sNum)
{
    bEsito = VerificaNumero(sNum);
    if (bEsito == true)
        return parseInt(sNum);
    for (a=0;a<3;a++)
        {sNum=prompt('Attenzione numero errato,Riensirisci il numero: ');
            bEsito = VerificaNumero(sNum);
        if (bEsito==true)
            return parseInt(sNum);
        }
    return null
}
const prompt = require('prompt-sync')();
var num1 = prompt('Inserisci il primo numeo: ');
var bEsito = VerificaNumero(num1)
var f = parseIntmy(num1)
if (f==null)
    console.log('hai inserito'+ f);
else
    console.log('non sei riuscito a inserire un num')
if(bEsito==true)
    console.log("Mi hai passato un numero")
else
    console.log("Non mi hai passato un  numero");

// var num1 = prompt('Inserisci il primo numeo: ');
// var num1corretto = controllo(num1)
// var num2 = prompt('Inserisci il secondo numero: ')





// var num1=parseInt(num1)
// var num2=parseInt(num2)
// console.log('somma:'+ (num1+num2))

// interface Point{
//     x:Number;
//     y:Number;
// }





// function logpoint