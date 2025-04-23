function solution(schedules, timelogs, startday) {
    const toSeconds = (t) => Math.floor(t/100)*60 + t%100
    
    const arriveTimes = schedules.map((t) => toSeconds(t)+10)
    let cnt = 0
    timelogs.forEach((times, idx) => {
        let day = startday
        let flag = true
        
        for (let i=0; i<times.length; i++){
            if (day === 6 || day === 7){
                day = day%7 + 1
                continue
            }
            if (toSeconds(times[i]) > arriveTimes[idx]){
                flag = false
                break
            }
            
            day = day%7 + 1
        }
        
        if (flag) cnt += 1
    })
    
    return cnt
}