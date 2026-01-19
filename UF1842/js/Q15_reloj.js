let manejador;

function mostrarFecha(){
    let fecha = new Date();
    let hora = fecha.getHours();
    let minutos = fecha.getMinutes();
    let segundos = fecha.getSeconds();
    let ano = fecha.getFullYear();
    let mes = fecha.getMonth();
    let diaSemana = fecha.get


let spanHora = document.getElementById("horas");
let spanMinutos = document.getElementById("minutos");
let spanSegundos = document.getElementById("segundos");

spanHora.innerHTML = hora.toString().padStart(2,'0');
spanMinutos.innerHTML = String(minutos).padStart(2,'0');
spanSegundos.innerHTML = segundos.toString().padStart(2,'0')

}

function Iniciar(){
    mostrarFecha();
    manejador = setInterval(mostrarFecha,1000);
}
function Parar(){
    clearInterval(manejador);
}
