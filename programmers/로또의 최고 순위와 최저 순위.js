function solution(lottos, win_nums) {
    const prizeInfo = { 6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6 };
    const zeroCount = lottos.reduce((acc, cur) => {
        if(cur === 0) return acc + 1;
        return acc;
    }, 0)

    const correctCount = lottos.reduce((acc, cur) => {
        if(cur === 0) return acc;
        if(win_nums.includes(cur)) return acc + 1;
        return acc;
    }, 0)

    return [prizeInfo[correctCount + zeroCount], prizeInfo[correctCount]]
}