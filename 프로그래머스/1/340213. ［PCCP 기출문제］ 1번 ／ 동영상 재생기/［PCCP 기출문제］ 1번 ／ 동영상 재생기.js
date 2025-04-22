function solution(video_len, pos, op_start, op_end, commands) {
    const to_seconds = (time_str) => {
        const m = time_str.split(":")[0]
        const s = time_str.split(":")[1]
        return Number(m)*60 + Number(s)
    }
        
    const video_total_sec = to_seconds(video_len)
    let pos_total_sec = to_seconds(pos)
    const op_start_total_sec = to_seconds(op_start)
    const op_end_total_sec = to_seconds(op_end)

    if (op_start_total_sec <= pos_total_sec && pos_total_sec < op_end_total_sec)
        pos_total_sec = op_end_total_sec
            
    commands.forEach((cmd) => {
        if (cmd === 'next')
            pos_total_sec = Math.min(video_total_sec, pos_total_sec + 10)
        else if (cmd === 'prev')
            pos_total_sec = Math.max(0, pos_total_sec - 10)
        
        if (op_start_total_sec <= pos_total_sec && pos_total_sec < op_end_total_sec)
            pos_total_sec = op_end_total_sec
    })
        
    return String(Math.floor(pos_total_sec/60)).padStart(2, 0) + ":" + String((pos_total_sec%60)).padStart(2, 0)
}