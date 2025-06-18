// Word Search Game
function wordSearchHTML(diff) {
    let size = diff==='easy'?6:diff==='hard'?12:8;
    return `<div id='wordSearchArea'></div>`;
}
function wordSearchInit(diff) {
    let size = diff==='easy'?6:diff==='hard'?12:8;
    const area = document.getElementById('wordSearchArea');
    let html = '<table style="margin:auto;border-collapse:collapse;">';
    for(let r=0;r<size;r++) {
        html+='<tr>';
        for(let c=0;c<size;c++) {
            html+=`<td style='border:1px solid #888;width:28px;height:28px;text-align:center;'>${String.fromCharCode(65+Math.floor(Math.random()*26))}</td>`;
        }
        html+='</tr>';
    }
    html+='</table>';
    area.innerHTML = html;
}
