// 0 또는 양의 정수가 주어졌을 때, 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.
// 예를 들어, 주어진 정수가 [6, 10, 2]라면 [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고, 
//이중 가장 큰 수는 6210입니다.
// 0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때, 순서를 재배치하여 만들 수 있는
// 가장 큰 수를 문자열로 바꾸어 return 하도록 solution 함수를 작성해주세요.

// numbers의 길이는 1 이상 100,000 이하입니다.
// numbers의 원소는 0 이상 1,000 이하입니다.
// 정답이 너무 클 수 있으니 문자열로 바꾸어 return 합니다.

// numbers	            return
// [6, 10, 2]	        "6210"
// [3, 30, 34, 5, 9]	"9534330"
function getMaxNumber(numbers: number[]) {

    var answer: string = '';

    answer = numbers.sort((a: any, b: any) => { //sort 함수 정의

        // string을 number로 합쳐 더 크면 내림차순 리턴
        let retVal1: number = Number(a + "" + b);
        let retVal2: number = Number(b + "" + a);

        return retVal1 < retVal2 ? 1 : -1;

    }).join('');

    //배열에 0밖에 없는경우, Ex>[0, 0, 0, 0, 0] 00000이 아닌 0 리턴 예외처리
    if (numbers.every(function (a: any) { return a == "0" })) {
        answer = "0";
    }

    return answer;
}

// getMaxNumber([0, 0, 0, 0, 0]);