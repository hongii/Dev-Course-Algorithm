function solution(routes) {
    routes.sort((a, b)=> a[1] - b[1]);
    
    let cnt = 0;
    let lastCam = -30001;
    routes.forEach(([s, e])=>{
        if(s > lastCam) {
            cnt += 1;
            lastCam = e
        }
    })
    
    return cnt
}