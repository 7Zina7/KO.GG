// Nonogram Game
function nonogramHTML(diff) {
    let size = diff==='easy'?5:diff==='hard'?12:8;
    return `<div id='nonogramArea'></div>`;
}
function nonogramInit(diff) {
    let size = diff==='easy'?5:diff==='hard'?12:8;
    const area = document.getElementById('nonogramArea');
    let html = `<table style='margin:auto;border-collapse:collapse;'>`;
    for(let r=0;r<size;r++) {
        html+='<tr>';
        for(let c=0;c<size;c++) {
            html+=`<td style='border:1px solid #888;width:22px;height:22px;text-align:center;'><button style='width:100%;height:100%;background:#fff;' onclick='this.style.background=\"#222\"'></button></td>`;
        }
        html+='</tr>';
    }
    html+='</table><div style="margin-top:8px;">Fill the grid as you like!</div>';
    area.innerHTML = html;
}
