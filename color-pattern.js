// Color Pattern Game
function colorPatternHTML(diff) {
    let len = diff==='easy'?4:diff==='hard'?8:6;
    return `<div id='colorPatternArea'></div>`;
}
function colorPatternInit(diff) {
    let len = diff==='easy'?4:diff==='hard'?8:6;
    const area = document.getElementById('colorPatternArea');
    let colors = ['red','green','blue','yellow','orange','purple'];
    let pattern = Array.from({length:len},()=>colors[Math.floor(Math.random()*colors.length)]);
    let user = [];
    let html = `<div style='display:flex;gap:8px;justify-content:center;margin-bottom:8px;'>`;
    colors.forEach(c=>{
        html += `<button class='cp-btn' data-color='${c}' style='width:36px;height:36px;background:${c};border-radius:50%;'></button>`;
    });
    html += '</div><button onclick="showPattern()">Show Pattern</button>';
    area.innerHTML = html;
    area.querySelectorAll('.cp-btn').forEach(btn=>{
        btn.onclick = function() {
            user.push(btn.dataset.color);
            if(user.length===pattern.length) {
                if(user.join()==pattern.join()) showGameMsg('You win!','success');
                else showGameMsg('Try again!','error');
                user=[];
            }
        }
    });
    window.showPattern = function() {
        let i=0;
        function flash() {
            if(i>=pattern.length) return;
            let btn = Array.from(area.querySelectorAll('.cp-btn')).find(b=>b.dataset.color===pattern[i]);
            btn.style.opacity = '0.5';
            setTimeout(()=>{btn.style.opacity='1';i++;flash();},350);
        }
        flash();
    }
}
