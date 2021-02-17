function solution(progresses, speeds) {
  let complete = [];

  // 각 몇일째에 완성되는지 구하기
  for (const [i, v] of progresses.entries()) {
    complete.push(Math.ceil((100 - progresses[i]) / speeds[i]));
  }

  // arr 돌면서 return값 구하기
  let max = complete[0];
  let res = [];
  let resIdx = 0;
  let val = 0;
  for (const [i, v] of complete.entries()) {
    if (v <= max) {
      val++;
      res[resIdx] = val;
    } else {
      val = 1;
      res[++resIdx] = val;
      max = v;
    }
  }
  return res;
}
