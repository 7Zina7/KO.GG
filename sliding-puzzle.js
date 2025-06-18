// Sliding Puzzle Game
function slidingPuzzleHTML(diff) {
    let size = diff==='easy'?3:diff==='hard'?5:4;
    return `<div class='sliding-puzzle ${diff}' id='slidingPuzzle'></div>`;
}
function slidingPuzzleInit(diff) {
    let size = diff==='easy'?3:diff==='hard'?5:4;
    const puzzle = document.getElementById('slidingPuzzle');
    let tiles = [...Array(size*size-1).keys()].map(x=>x+1).concat(['']);
    do {
        tiles = shuffle(tiles);
    } while(!isSolvable(tiles, size));
    render();
    function render() {
        puzzle.innerHTML = '';
        tiles.forEach((val, i) => {
            const div = document.createElement('div');
            div.className = 'sliding-tile' + (val === '' ? ' empty' : '');
            div.textContent = val;
            div.onclick = () => move(i);
            puzzle.appendChild(div);
        });
    }
    function move(i) {
        const empty = tiles.indexOf('');
        const row = idx => Math.floor(idx/size);
        const col = idx => idx%size;
        let moved = false;
        // Allow sliding in row or column if path is clear
        if(row(i) === row(empty)) {
            const [start, end] = [i, empty].sort((a,b)=>a-b);
            if(tiles.slice(start+1,end).every((_,j)=>tiles[start+1+j]==='')) return showGameMsg('Not possible', 'error');
            if(i < empty) {
                for(let j=empty;j>i;j--) tiles[j]=tiles[j-1];
            } else {
                for(let j=empty;j<i;j++) tiles[j]=tiles[j+1];
            }
            tiles[i]='';
            moved = true;
        } else if(col(i) === col(empty)) {
            const [start, end] = [i, empty].sort((a,b)=>a-b);
            let clear = true;
            for(let j=start+size;j<end;j+=size) if(tiles[j]!=='') clear=false;
            if(!clear) return showGameMsg('Not possible', 'error');
            if(i < empty) {
                for(let j=empty;j>i;j-=size) tiles[j]=tiles[j-size];
            } else {
                for(let j=empty;j<i;j+=size) tiles[j]=tiles[j+size];
            }
            tiles[i]='';
            moved = true;
        } else {
            return showGameMsg('Not possible', 'error');
        }
        if(moved) {
            render();
            if(tiles.join() === [...Array(size*size-1).keys()].map(x=>x+1).concat(['']).join())
                setTimeout(()=>showGameMsg('You solved it!', 'success'), 100);
        }
    }
    function shuffle(a) {
        for(let i=a.length-1;i>0;i--) {
            const j=Math.floor(Math.random()*(i+1));
            [a[i],a[j]]=[a[j],a[i]];
        }
        return a;
    }
    function isSolvable(arr, size) {
        let inv=0;
        for(let i=0;i<arr.length-1;i++) for(let j=i+1;j<arr.length;j++)
            if(arr[i]&&arr[j]&&arr[i]>arr[j]) inv++;
        if(size%2===1) return inv%2===0;
        const row = Math.floor(arr.indexOf('')/size);
        return (inv + row)%2===1;
    }
}
