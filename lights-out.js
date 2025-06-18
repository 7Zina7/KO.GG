// Lights Out Game
function lightsOutHTML(diff) {
    let size = diff==='easy'?3:diff==='hard'?7:5;
    return `<div id='lightsOutArea'></div>`;
}
function lightsOutInit(diff) {
    let size = diff==='easy'?3:diff==='hard'?7:5;
    const area = document.getElementById('lightsOutArea');
    let board = Array(size*size).fill().map(()=>Math.random()<0.5?1:0);
    render();
    function render() {
        let html = `<div style='display:grid;grid-template-columns:repeat(${size},32px);gap:4px;margin:auto;'>`;
        board.forEach((v,i)=>{
            html += `<button class='lo-btn' data-idx='${i}' style='width:32px;height:32px;background:${v?'#ffd700':'#333'};'></button>`;
        });
        html += '</div>';
        area.innerHTML = html;
        area.querySelectorAll('.lo-btn').forEach(btn=>{
            btn.onclick = function() {
                const idx = +btn.dataset.idx;
                [idx,idx-1,idx+1,idx-size,idx+size].forEach(j=>{
                    if(j>=0&&j<board.length&&((Math.abs(j-idx)===1&&Math.floor(j/size)===Math.floor(idx/size))||Math.abs(j-idx)===size||j===idx))
                        board[j]=1-board[j];
                });
                render();
                if(board.every(x=>x===0)) setTimeout(()=>alert('You win!'),100);
            }
        });
    }
}
