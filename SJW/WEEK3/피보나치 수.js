function solution(n) {

    return fibonacci(n) ;
}
// F(N) % 1234567 = ( F(N-1) % 1234567 + F(N-2) % 1234567 ) % 1234567 이게 성립하네요.
function fibonacci(n) {
    if (n < 2)
        return n ;
    else
        return (fibonacci(n - 1) % 1234567  + fibonacci(n - 2) % 1234567) % 1234567;
}



function solution(n) {
    var answer = 0;
    const dp = [0, 1, 1];

    for (let i = 2; i <= n; ++i) {
        dp[i] = (dp[i - 1] + dp[i - 2]) % 1234567;
    }

    return dp[n];
}


solution(0);