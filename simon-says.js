// Simon Says Game
function simonSaysHTML(diff) {
    let steps = diff==='easy'?4:diff==='hard'?9:6;
    return `<div id='simonArea'></div>`;
}
function simonSaysInit(diff) {
    let steps = diff==='easy'?4:diff==='hard'?9:6;
    const area = document.getElementById('simonArea');
    let colors = ['red','green','blue','yellow'];
    let sequence = Array.from({length:steps},()=>colors[Math.floor(Math.random()*4)]);
    let userSeq = [], idx = 0;
    let html = `<div style='display:flex;gap:8px;justify-content:center;margin-bottom:8px;'>`;
    colors.forEach(c=>{
        html += `<button class='simon-btn' data-color='${c}' style='width:48px;height:48px;background:${c};border-radius:50%;'></button>`;
    });
    html += "</div><button onclick=\"playSeq()\">Play Sequence</button>";
    area.innerHTML = html;
    area.querySelectorAll('.simon-btn').forEach(btn=>{
        btn.onclick = function() {
            userSeq.push(btn.dataset.color);
            if(userSeq[userSeq.length-1]!==sequence[userSeq.length-1]) {
                showGameMsg('Wrong!','error'); userSeq=[]; idx=0;
            } else if(userSeq.length===sequence.length) {
                showGameMsg('You win!','success');
            }
        }
    });
    window.playSeq = function() {
        let i=0;
        function flash() {
            if(i>=sequence.length) return;
            let btn = Array.from(area.querySelectorAll('.simon-btn')).find(b=>b.dataset.color===sequence[i]);
            btn.style.opacity = '0.5';
            setTimeout(()=>{btn.style.opacity='1';i++;flash();},400);
        }
        flash();
    }
}
