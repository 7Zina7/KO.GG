// Memory Match Game
function memoryMatchHTML(diff) {
    let pairs = diff==='easy'?3:diff==='hard'?10:6;
    return `<div id='memoryArea'></div>`;
}
function memoryMatchInit(diff) {
    let pairs = diff==='easy'?3:diff==='hard'?10:6;
    const area = document.getElementById('memoryArea');
    let cards = Array.from({length:pairs},(_,i)=>i+1).flatMap(x=>[x,x]);
    cards = shuffle(cards);
    let html = '<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(48px,1fr));gap:8px;max-width:300px;margin:auto;">';
    cards.forEach((v,i)=>{
        html += `<button class='memcard' data-idx='${i}' style='height:48px;font-size:1.2rem;'>?</button>`;
    });
    html += '</div>';
    area.innerHTML = html;
    let flipped = [], matched = [];
    area.querySelectorAll('.memcard').forEach(btn=>{
        btn.onclick = function() {
            const idx = +btn.dataset.idx;
            if(flipped.length<2 && !flipped.includes(idx) && !matched.includes(idx)) {
                btn.textContent = cards[idx];
                flipped.push(idx);
                if(flipped.length===2) {
                    setTimeout(()=>{
                        if(cards[flipped[0]]===cards[flipped[1]]) {
                            matched.push(...flipped);
                            if(matched.length===cards.length) showGameMsg('You win!','success');
                        } else {
                            flipped.forEach(i=>area.querySelectorAll('.memcard')[i].textContent='?');
                            showGameMsg('No match','error');
                        }
                        flipped=[];
                    }, 700);
                }
            } else if (matched.includes(idx)) {
                showGameMsg('Already matched','info');
            } else if (flipped.includes(idx)) {
                showGameMsg('Already flipped','info');
            }
        }
    });
}
function shuffle(a) {
    for(let i=a.length-1;i>0;i--) {
        const j=Math.floor(Math.random()*(i+1));
        [a[i],a[j]]=[a[j],a[i]];
    }
    return a;
}
function showGameMsg(msg,type) {
    const colors = {success:'green',error:'red',info:'blue'};
    let msgDiv = document.getElementById('gameMsg');
    if(!msgDiv) {
        msgDiv = document.createElement('div');
        msgDiv.id = 'gameMsg';
        msgDiv.style.position = 'fixed';
        msgDiv.style.top = '10px';
        msgDiv.style.left = '50%';
        msgDiv.style.transform = 'translateX(-50%)';
        msgDiv.style.padding = '10px 20px';
        msgDiv.style.borderRadius = '5px';
        msgDiv.style.color = 'white';
        msgDiv.style.zIndex = '1000';
        document.body.appendChild(msgDiv);
    }
    msgDiv.textContent = msg;
    msgDiv.style.backgroundColor = colors[type] || 'black';
    msgDiv.style.display = 'block';
    setTimeout(()=>msgDiv.style.display='none',2000);
}
