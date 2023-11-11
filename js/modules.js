function adjustForMobile() {
    if (screen.width <= 699) {
        [...document.querySelectorAll('.side-spacer')].forEach(e=>e.remove());
        [...document.querySelectorAll('.spacer-container')].forEach(e=>{
            e.style.display = 'block';
            e.gridTemplateColumns = 'none';
        });

        [...document.querySelectorAll('img-tabs')].forEach(e=>{
            const contentWidth = [...e.childNodes[0].childNodes].reduce((a,div)=>(a + Number(div.clientWidth)), 0);
            e.style.transformOrigin = "left top";
            e.style.scale = (screen.width / contentWidth)*0.88;
            console.log("contentWidth: "+contentWidth);
            console.log("screen.width: "+screen.width);
        });

    }

}


addEventListener("DOMContentLoaded", adjustForMobile);