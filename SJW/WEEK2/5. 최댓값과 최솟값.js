function solution(s) {
    var answer = '';

    let arr =  s.split(" ");    //구분자로 짜름

    for(let i in arr){
        arr[i] =  arr[i]*=1; //형변환
    }

    let arr2 = [];

    arr2.push(Math.min.apply(null,arr));    //최솟값 apply함수 이용 배열전달
    arr2.push(Math.max.apply(null,arr));    //최대값 apply함수 이용 배열전달

    answer = arr2.join(" "); //다시 합침

    return answer;
}
solution("1 2 3 4");