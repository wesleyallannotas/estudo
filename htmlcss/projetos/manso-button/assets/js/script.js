function alertaManso() {
    let mansoText = document.getElementById('alerta-manso');
    let mansoSong = document.querySelector('audio');
    mansoText.innerHTML = "Impossivel<br/>Nivel de mansidao muito alto!!";
    mansoSong.play();
}