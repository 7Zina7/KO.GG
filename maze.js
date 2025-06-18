// Maze Solver Game
function mazeHTML(diff) {
    let size = diff==='easy'?5:diff==='hard'?12:8;
    return `<div id='mazeArea'></div>`;
}
function mazeInit(diff) {
    let size = diff==='easy'?5:diff==='hard'?12:8;
    const area = document.getElementById('mazeArea');
    let html = `<table style='margin:auto;border-collapse:collapse;'>`;
    for(let r=0;r<size;r++) {
        html+='<tr>';
        for(let c=0;c<size;c++) {
            let cell = (r===0&&c===0)?'S':(r===size-1&&c===size-1)?'E':'';
            html+=`<td style='border:1px solid #888;width:28px;height:28px;text-align:center;'>${cell}</td>`;
        }
        html+='</tr>';
    }
    html+='</table><div style="margin-top:8px;">Use your imagination to solve!</div>';
    area.innerHTML = html;
}
