function solution(price, money, count) {
    for(let i = 0; i < count; i ++){
        money -= price * (i+1);
    }
    return money < 0 ? Math.abs(money) : 0;
}