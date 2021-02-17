//
//  main.cpp
//  WEEK2_2
//  프로그래머스(LV2.스택/큐> 기능개발)
//  Created by 장병윤 on 2021/02/15.
//

#include <iostream>
#include <vector>
#include <queue>

/*
int main(int argc, const char * argv[]) {
    // insert code here...
    std::cout << "Hello, World!\n";
    return 0;
}
*/

using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> answer;
    queue<int> q;
    
    for(int i=0; i<progresses.size(); i++)
    {
        int dayCnt = 0;
        while(progresses[i] < 100) // 며칠이 걸리는지 계산.
        {
            progresses[i] += speeds[i];
            dayCnt++;
        }
        q.push(dayCnt);
    }

    int cnt = 1;
    int now = q.front();
    q.pop();
    
    
    while (!q.empty()) { //큐의 맨 앞 값과 현재 값 비교해서 cnt 카운팅.
        if(q.front() <= now)
        {
            q.pop();
            cnt++;
        }
        else
        {
            answer.push_back(cnt);
            cnt = 1;
            now = q.front();
            q.pop();
        }
    }
    
    answer.push_back(cnt);
    
    return answer;
}
