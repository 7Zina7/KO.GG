// Towers of Hanoi Game
function hanoiHTML(diff) {
    let disks = diff==='easy'?3:diff==='hard'?5:4;
    return `<div id='hanoiArea'></div>`;
}
function hanoiInit(diff) {
    let disks = diff==='easy'?3:diff==='hard'?5:4;
    const area = document.getElementById('hanoiArea');
    let towers = [Array.from({length:disks},(_,i)=>disks-i),[],[]];
    render();
    let selected = null;
    function render() {
        let html = '<div style="display:flex;gap:16px;justify-content:center;">';
        towers.forEach((tower,ti)=>{
            html += `<div style='min-width:48px;'><div>T${ti+1}</div>`;
            tower.slice().reverse().forEach((disk,di)=>{
                html += `<div style='background:#bfa;width:${disk*18}px;height:18px;margin:2px auto;border-radius:4px;text-align:center;'>${disk}</div>`;
            });
            html += `<button onclick='moveDisk(${ti})'>Select</button></div>`;
        });
        html += '</div>';
        area.innerHTML = html;
    }
    window.moveDisk = function(ti) {
        if(selected===null) {
            if(towers[ti].length) selected=ti;
        } else {
            if(ti!==selected && (!towers[ti].length || towers[ti][towers[ti].length-1]>towers[selected][towers[selected].length-1])) {
                towers[ti].push(towers[selected].pop());
                if(towers[2].length===disks) setTimeout(()=>alert('You win!'),100);
            }
            selected=null;
        }
        render();
    }
}
