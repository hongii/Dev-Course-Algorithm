function solution(targets) {
    targets.sort((a, b) => a[1]-b[1]);
    
    let cnt = 0;
    let lastX = -1;
    targets.forEach(([s, e]) => {
        if (lastX <= s){
            lastX = e;
            cnt++;
        }
    })
    
    return cnt
}