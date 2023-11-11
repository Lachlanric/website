function adjustForMobile() {
    if (screen.width <= 699) {
        [...document.querySelectorAll('.side-spacer').forEach(e=>e.remove())];
        [...document.querySelectorAll('.spacer-container').forEach(e=>{
            e.style.display = 'block';
            e.gridTemplateColumns = 'none';
        })];

    }

    alert("screen.width: "+screen.width);
}


addEventListener("DOMContentLoaded", adjustForMobile);

