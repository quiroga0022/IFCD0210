let manejador;

function mostrarFecha(){
    let fecha = new Date();
    let hora = fecha.getHours();
    let minutos = fecha.getMinutes();
    let segundos = fecha.getSeconds();
    let diames = fecha.getDate();
    let mes = fecha.getMonth()+1;
    let diasemana = fecha.getDay();


    let spanHora = document.getElementById("horas");
    let spanMinutos = document.getElementById("minutos");
    let spanSegundos = document.getElementById("segundos");
    let spanDiames = document.getElementById("diames");
    let spanMes = document.getElementById("mes");
    let spanDiasemana = document.getElementById("diasemana");

    spanHora.innerHTML = hora.toString().padStart(2,'0');
    spanMinutos.innerHTML = String(minutos).padStart(2,'0');
    spanSegundos.innerHTML = segundos.toString().padStart(2,'0');
    spanDiames.innerHTML = diames.toString().padStart(2,'0'); 
    spanMes.innerHTML = mes.toString().padStart(2,'0');
    spanDiasemana.innerHTML = diaSemana(diasemana);

}

function Iniciar(){
    mostrarFecha();
    manejador = setInterval(mostrarFecha,1000);
}
function Parar(){
    clearInterval(manejador);
}
function diaSemana(numDia){
    let semana = ['Domingo','Lunes','Martes','Miercoles','Jueves','Viernes','Sábado'];
    return semana[numDia];
}
