function fazSequencia(valor){
    let cont =1;
    while (valor > 1){
        if(valor % 2 === 0){
            valor = valor / 2;
        }else{
            valor = (valor *3)+1

        }
        cont++
    }
    return cont;
}


let numeroMaior;
let maiorSequencia =0

for (let i=1; i < 1000000; i++){
    let sequencia = fazSequencia(i);
    if(sequencia > maiorSequencia){
        maiorSequencia = sequencia;
        numeroMaior = i;
    }
    
}
console.log( `Numero com maior sequencia: ${ numeroMaior } `);
console.log(`Sequencia obtida: ${maiorSequencia}`);