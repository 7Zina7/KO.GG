// Sudoku Mini Game
function sudokuHTML(diff) {
    let size = diff==='easy'?4:diff==='hard'?9:6;
    return `<div id='sudokuArea'></div>`;
}
function sudokuInit(diff) {
    let size = diff==='easy'?4:diff==='hard'?9:6;
    const area = document.getElementById('sudokuArea');
    let board = Array(size*size).fill('');
    for(let i=0;i<size;i++) board[i*size+i] = ((i+1)%size)+1;
    let html = `<table style='margin:auto;border-collapse:collapse;'>`;
    for(let r=0;r<size;r++) {
        html += '<tr>';
        for(let c=0;c<size;c++) {
            html += `<td style='border:1px solid #888;width:32px;height:32px;text-align:center;'>`;
            html += `<input type='text' maxlength='1' style='width:28px;text-align:center;font-size:1rem;' value='${board[r*size+c]||''}'></td>`;
        }
        html += '</tr>';
    }
    html += '</table>';
    area.innerHTML = html;
}
