function solution(n, computers) {
    const graph = Array.from({length:n}, ()=>[]);
    let cnt = 0;
    const visited = Array(n).fill(false);
    
    computers.forEach((comp, i)=>{
        for(let j=0; j<n; j++){
            if(i === j) continue;
            if(comp[j] === 1) graph[i].push(j);
        }
    })
    
    const bfs = (x) => {
        visited[x] = true;
        const q = [x];
        
        while(q.length) {
            const node = q.shift();
            
            for (const next of graph[node]) {
                if (!visited[next]) {
                    visited[next] = true;
                    q.push(next);
                }
            }
        }
    }
    
    for (let i=0; i<n; i++){
        if(!visited[i]){
            bfs(i);
            cnt++; 
        }
    }
    return cnt
}