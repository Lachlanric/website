function displayImg(img_tabs_id,img_id) {
    // Set --disp property to true if it's the image clicked on, otherwise false
    [...document.querySelectorAll(`#img-tab-large-${img_tabs_id} > img`)].forEach(e=>{
        e.style.setProperty('--disp', Number(e.id==`img-large-${img_tabs_id}-${img_id}`));
    });

    [...document.querySelectorAll(`#img-tab-preview-${img_tabs_id} > div > img`)].forEach(e=>{
        e.style.opacity = e.id==`img-preview-${img_tabs_id}-${img_id}` ? String(1) : String(0.5);
    });
}


function parseImgTabs() {

    [...document.querySelectorAll('img-tabs')].forEach(((img_tabs,i)=>{

        const imgs = [...img_tabs.querySelectorAll('img')];
        const width = Number(img_tabs.getAttribute('res-width'));
        const height = Number(img_tabs.getAttribute('res-height'));
        const margin = 2;

        let small_height;
        let small_width;

        if (imgs.length >= 4) {
            small_height = Math.floor( height / imgs.length ) - 0.5*margin*imgs.length;
            small_width = Math.floor( small_height * (width/height) );
        } else {
            small_width = Math.floor( width/4 - 0.5*margin*imgs.length );
            small_height = Math.floor( small_width * (height/width) );
        }

        console.log(height, width);
        console.log(small_height, small_width);

        const small_str = 
            `<div id="img-tab-preview-${i}" style="grid-column: 1";>`
                + imgs.map((img,j)=>`<div><img id="img-preview-${i}-${j}" src="${img.src}" class="littlebox" style="margin: ${margin}px; height: ${small_height}px; width: ${small_width}px;" onclick="displayImg(${i},${j});"></img></div>`).reduce((a,c)=>a+c)
                + `</div>`;

        const large_str = 
            `<div id="img-tab-large-${i}" style="grid-column: 2; position: relative; width: ${width}px; height: ${height}px; border: solid black 5px; padding: 0; background-color: beige">`
                + imgs.map((img,j)=>`<img id="img-large-${i}-${j}" src="${img.src}" class="bigbox"></img>`).reduce((a,c)=>a+c)
                + `</div>`;

        img_tabs.innerHTML = 
            `<div style="display: grid; grid-template-columns: ${small_width+margin+10}px auto;">`
                + small_str
                + large_str;
                + `</div>`;
        
        img_tabs.style.display = "block";
        img_tabs.querySelector('img').click();

    }));
    
}

window.onload = parseImgTabs;