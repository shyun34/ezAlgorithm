// 네트워크란 컴퓨터 상호 간에 정보를 교환할 수 있도록 연결된 형태를 의미합니다.
// 예를 들어, 컴퓨터 A와 컴퓨터 B가 직접적으로 연결되어있고, 
// 컴퓨터 B와 컴퓨터 C가 직접적으로 연결되어 있을 때 컴퓨터 A와 컴퓨터 C도 간접적으로 연결되어 정보를 교환할 수 있습니다. 
// 따라서 컴퓨터 A, B, C는 모두 같은 네트워크 상에 있다고 할 수 있습니다.

// 컴퓨터의 개수 n, 연결에 대한 정보가 담긴 2차원 배열 computers가 매개변수로 주어질 때, 
// 네트워크의 개수를 return 하도록 solution 함수를 작성하시오.

// 컴퓨터의 개수 n은 1 이상 200 이하인 자연수입니다.
// 각 컴퓨터는 0부터 n-1인 정수로 표현합니다.
// i번 컴퓨터와 j번 컴퓨터가 연결되어 있으면 computers[i][j]를 1로 표현합니다.
// computer[i][i]는 항상 1입니다.


function solution(n, computers) { //n=3 ,computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    var answer = 0;

    let networkNodes = [];  //네트워크 노드들

    for (let i = 0; i < n; i++) {
       
        if (networkNodes.length < 1) {

            networkNodes.push(computers[i]); //노드가 하나도 없으면 추가

        } else {
            let isAllNotConnected = [];

            for (let j = 0; j < networkNodes.length; j++) { //노드 수만큼 반복

                let isConnected = false; //하나라도 연결되어있는지 나타내는 플래그 값

                for (let k = 0; k < n; k++) { //노드의 각 항목비교
                    if ((networkNodes[j][k] === 1 && computers[i][k] === 1) && networkNodes[j][k] === computers[i][k]) {

                        isConnected = true; //노트의 각항목이 하나라도 겹치면 연결되어있는 것
                    }
                }

                if (isConnected) { //노트의 각항목이 하나라도 겹치면 연결되어있는 것

                    for (let k = 0; k < n; k++) { //노드의 각 항목비교
                        networkNodes[j][k] = networkNodes[j][k] === 1 ? 1 : computers[i][k] === 1 ? 1 : 0; //합치는 과정
                    }
                    isAllNotConnected.push(false); 

                } else {
                    isAllNotConnected.push(true); 
                }
            }

            if (isAllNotConnected.length > 0 && isAllNotConnected.every((x) => x === true)) { //아무 노드랑도 안겹치면 추가
                networkNodes.push(computers[i]);  //새로운 노드 추가
            }
        }
    }
    answer = networkNodes.length;

    return answer;
}

solution(5, [[1, 1, 0, 0, 1], [1, 1, 0, 0, 0], [0, 0, 1, 0, 1], [0, 0, 0, 1, 1], [1, 0, 1, 1, 1]]); //1
solution(4, [[1, 0, 0, 1], [0, 1, 0, 1], [0, 0, 1, 0], [1, 1, 0, 1]]); //2
solution(4, [[1, 0, 1, 0], [0, 1, 0, 1], [1, 0, 1, 0], [0, 1, 0, 1]]); //2

