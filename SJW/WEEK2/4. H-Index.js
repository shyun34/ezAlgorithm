// H-Index는 과학자의 생산성과 영향력을 나타내는 지표입니다. 어느 과학자의 H-Index를 나타내는 값인 h를 구하려고 합니다. 
// 위키백과1에 따르면, H-Index는 다음과 같이 구합니다.
// 어떤 과학자가 발표한 논문 n편 중, h번 이상 인용된 논문이 h편 이상이고 나머지 논문이 h번 이하 인용되었다면 h의 최댓값이 이 과학자의 H-Index입니다.
// 어떤 과학자가 발표한 논문의 인용 횟수를 담은 배열 citations가 매개변수로 주어질 때, 이 과학자의 H-Index를 return 하도록 solution 함수를 작성해주세요.

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
