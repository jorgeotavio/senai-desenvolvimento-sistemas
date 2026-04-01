function sleepBlock(milliseconds) {
    
    const date = Date.now();
    let currentDate = 0;

    while ((currentDate - date) < milliseconds) {
        currentDate = Date.now();
        console.log('Timestamp atual', currentDate);
        
    }
}

let indicator = 0

while (indicator < 2) {
    sleepBlock(4000) // pausa o código durante 4 segundos
    indicator = indicator + 1
    console.log('Passou o tempo', indicator);
}



function getTemperaturaDaPiscina () {
    return 45
}


let temperaturaDaPiscina = getTemperaturaDaPiscina()

const temperaturaIdeal = 30
const margemDeErro = 2

const estaFria = temperaturaDaPiscina < (temperaturaIdeal - margemDeErro)
const estaQuente = temperaturaDaPiscina > (temperaturaIdeal + margemDeErro)

const temperaturaEstaIdeal = !estaFria && !estaQuente

if (temperaturaEstaIdeal) {
    console.log('Nao faz nada')
}

if(estaFria) {
    console.log('Esquento')
}

if(estaQuente) {
    console.log('Esfria')
}

