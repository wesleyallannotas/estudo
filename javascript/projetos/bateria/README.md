Segundo parâmetro de EventListener e um função pode ser criada ali mesmo, ou podemos criar a função fora também.  
```javascript
document.body.addEventListener('keyup', (event)=>{
    playSound(event.code.toLowerCase());
});

document.querySelector('.composer button').addEventListener('click', ()=>{
    let song = document.querySelector('#input').value;

    if(song !== '') {
        let songArray = song.split(''); // Como nao tem um separador, separa por cada carácter.
        playComposition(songArray);
    }
})

function playSound(sound) {
    let audioElement = document.querySelector(`#s_${sound}`);
    let keyElement = document.querySelector(`div[data-key="${sound}"]`);
    
    // Verifica para tocar
    if(audioElement) {
        audioElement.currentTime = 0;
        audioElement.play();
    }
    // Verifica para pisca
    if(keyElement) {
        keyElement.classList.add('active');
        setTimeout(()=>{
            keyElement.classList.remove('active');
        }, 300);
    }
};

function playComposition(songArray) {
    let wait = 0;

    for(let songItem of songArray) {
        setTimeout(()=>{    // Timer para nao tocar tudo de uma vez.
        playSound(`key${songItem}`);
        }, wait);
        wait += 250;
    }
}
```