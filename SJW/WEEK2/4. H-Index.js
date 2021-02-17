function solution(citations) {
    let answer = 0;
    for(let n = citations.length; n > 0 ; n--){
        //n편 중, h번 이상 인용된 논문이 h편 이상이면 h의 최댓값이 이 과학자의 H-Index
        if(citations.filter(value => value >= n).length >= n){
            answer = n;
            break;
        }
    }
    return answer;
}


solution([4, 4, 4, 5, 0, 1, 2, 3] );
// [12, 11, 10, 9, 8, 1] 5
// [6, 6, 6, 6, 6, 1] 5
// [4, 4, 4] 3
// [4, 4, 4, 5, 0, 1, 2, 3] 4
// [10, 11, 12, 13] 4
// [3, 0, 6, 1, 5] 3
// [0, 0, 1, 1] 1
// [0, 1] 1
// [10, 9, 4, 1, 1] 3
