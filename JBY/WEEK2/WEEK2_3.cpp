//
//  main.cpp
//  WEEK2_3
//  프로그래머스(LV2.정렬/H-Index)
//  Created by 장병윤 on 2021/02/16.
//

#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int solution(vector<int> citations) {
    int answer = 0;
    
    sort(citations.begin(), citations.end(), greater<int>());
    
    for(int i=0; i<citations.size(); i++)
    {
        if(i + 1 <= citations[i])
        {
            answer = i + 1;
        }
        else
        {
            break;
        }
    }
    
    return answer;
}
