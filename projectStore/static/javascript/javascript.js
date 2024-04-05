const hoverImgs = document.querySelectorAll('.colorsCard div img');
const imgContainer = document.querySelector('.imgContainer');

window.addEventListener('DOMContentLoaded', () =>{

    hoverImgs[0].parentElement.classList.add('active');
})

hoverImgs.forEach((image) => {
    image.addEventListener('mouseover',()=>{
        imgContainer.querySelector('img').src = image.src;
        image.parentElement.classList.add('active')

    })
})

function resetActiveImg(){

    hoverImgs.forEach((img)=>{
        img.parentElement.classList.remove('active');

    })
}