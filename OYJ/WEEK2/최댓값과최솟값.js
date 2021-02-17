function solution(s) {
  const sarr = s.split(" ");
  return [Math.min(...sarr), Math.max(...sarr)].join(" ");
}
