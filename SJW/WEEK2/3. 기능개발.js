function solution(progresses, speeds) {
    var answer = [];

    while (progresses.length) { //배열이 있는동안

        for (let i = 0; i < progresses.length; i++) { //각 스피드만큼 더해준다
            progresses[i] += speeds[i];
        }

        let cnt = 0; //뺄만큼의 수
        for (let i = 0; i < progresses.length; i++) {
            if (progresses[i] >= 100) { //100프로 넘었으면 뺄거 더해줌
                cnt++;
            } else {    //아니면 반복 나옴
                break;
            }
        }

        if (cnt > 0) {  //뺄게있으면
            for(let i = 0 ; i < cnt; i++){ 
                progresses.shift(0);    //배열에서 빼줌
                speeds.shift(0);        //스피드도 배열만큼이여햐하니까 빼줌
            }
            answer.push(cnt);
        }
    }
    return answer;
}