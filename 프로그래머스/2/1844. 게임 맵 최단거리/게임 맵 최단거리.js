function solution(maps) {
    const row = maps.length, col = maps[0].length;
    const dist = Array.from({length:row}, () => Array.from({length:col}, () => Infinity));
    const dx = [-1, 0, 1, 0];
    const dy = [0, 1, 0, -1];
    
    const isCheck = (x, y) => 0 <= x && x < row && 0 <= y && y < col;
    
    const bfs = (a, b) => {
        dist[a][b] = 1;
        const q = [[a, b]];
        
        while(q.length){
            const [x, y] = q.shift();
            
            for(let i=0; i<4; i++){
                const x_ = dx[i] + x;
                const y_ = dy[i] + y;
                
                if(isCheck(x_, y_) && dist[x_][y_] > dist[x][y]+1 && maps[x_][y_] === 1){
                    q.push([x_, y_]);
                    dist[x_][y_] = dist[x][y]+1;
                }
            }
        }
    }
    
    bfs(0, 0);
    return dist[row-1][col-1] !== Infinity ? dist[row-1][col-1] : -1; 
}