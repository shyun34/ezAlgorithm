// 어떤 숫자에서 k개의 수를 제거했을 때 얻을 수 있는 가장 큰 숫자를 구하려 합니다.

// 예를 들어, 숫자 1924에서 수 두 개를 제거하면 [19, 12, 14, 92, 94, 24] 를 만들 수 있습니다. 
// 이 중 가장 큰 숫자는 94 입니다.

// 문자열 형식으로 숫자 number와 제거할 수의 개수 k가 solution 함수의 매개변수로 주어집니다. 
// number에서 k 개의 수를 제거했을 때 만들 수 있는 수 중 가장 큰 숫자를 
// 문자열 형태로 return 하도록 solution 함수를 완성하세요.

function solution(number, k) {
    const n = number.length;
    let answer = '',
        startIdx = 0,
        maxChar,
        maxIdx = 0;

    for (let i = n - k; i > 0; i--) {  // i = 6
        
        maxChar = '0';

        for (let j = startIdx; j <= n - i; j++) { // 0 ~ 4
            if (number[j] > maxChar) {
                maxIdx = j;
                maxChar = number[j];
                if (maxChar === '9') {
                    break;
                }
            }
        }

        answer += maxChar;
        startIdx = maxIdx + 1;
    }

    return answer;
  }
  solution("4177252841" , 4);
  //41772  --> 7    :             41772 52841
  //725    --> 7    : 417           725 2841
  //252    --> 5    : 417 7         252 841
  //28     --> 8    : 417 7 25       28 41
  //4      --> 4    : 417 7 25 2 8    4 1
  //1      --> 1    : 417 7 25 2 8 4  1