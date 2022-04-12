var image = ["1" , "2" , "3"];
var container = document.querySelector('.container');
var body = document.querySelector('.body');
var index = 1;

function forward(){
    index++;
    if(index > image.length){
        index=1;
    };
    container.style.backgroundImage = `url('./assets/images/${index}.jpg')`;
    body.style.backgroundImage = `url('./assets/images/fundo${index}.jpg')`;
    

}
function backward(){
    index--;
    if(index < 1){
        index= 3;
    };
    container.style.backgroundImage = `url('./assets/images/${index}.jpg')`;
    body.style.backgroundImage = `url('./assets/images/fundo${index}.jpg')`;
}
