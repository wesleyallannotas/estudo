let digitalElement = document.querySelector('.digital'); 
let sElement = document.querySelector('.p_s');
let mElement = document.querySelector('.p_m');
let hElement = document.querySelector('.p_h');

function updateClock() {
    let now = new Date();
    let hour = now.getHours();
    let minute = now.getMinutes();
    let second = now.getSeconds();
    
    // Relógio Digital
    digitalElement.innerHTML = `${fixZero(hour)}:${fixZero(minute)}:${fixZero(second)}`;
    
    // Relógio Analógico
    let sDeg = ((360 / 60) * second) - 90; // - 90 para corrigir o posicionamento padrão.
    let mDeg = ((360 / 60) * minute) - 90; 
    let hDeg = ((360 / 12) * hour) - 90; 

    sElement.style.transform = `rotate(${sDeg}deg)`;
    mElement.style.transform = `rotate(${mDeg}deg)`;
    hElement.style.transform = `rotate(${hDeg}deg)`;
}

function fixZero(time) {
    // if(time < 10) {
    //     return '0'+time;
    // } else {
    //     return time;
    // }

    // Com apenas uma linha o mesmo resultado
    return time < 10 ? `0${time}` : time;
}

setInterval(updateClock, 1000);
updateClock();