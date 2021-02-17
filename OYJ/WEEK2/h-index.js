function solution(citations) {
  // 내림차순 정렬
  for (const [idx, citation] of citations.sort((a, b) => b - a).entries()) {
    if (citation <= idx) return idx;
  }

  // 테스트 9번 통과못함
}
