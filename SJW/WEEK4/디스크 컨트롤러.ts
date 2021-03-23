function solution1(jobs: Array<Array<number>>): number {
    var answer = 0;

    jobs.sort((a: Array<number>, b: Array<number>) => {

        let caseA: number = (a[0] + a[1]) * 2 + b[1];
        let caseB: number = (b[0] + b[1]) * 2 + a[1];

        let retVal: number = 0;

        if (caseA > caseB) retVal = 1;
        if (caseA === caseB) retVal = 0;
        if (caseA < caseB) retVal = -1;

        return retVal;
    })

    let cur = jobs[0][0];
    let sum = 0;

    for (let i = 0; i < jobs.length; i++) {

        if(cur < jobs[i][0]){
            cur = jobs[i][0] + jobs[i][1];
            sum += cur - jobs[i][0];
        }else{
           cur += jobs[i][1];
            sum += cur - jobs[i][0];
        }

    }

    answer = Math.floor(sum/jobs.length);

    return answer;
}

solution1([[0, 10], [2,10], [9,10], [15,2]]  );