//
//  main.cpp
//  WEEK4_1
//  프로그래머스 LV2 > 가장 큰 수
//  Created by 장병윤 on 2021/03/21.
//

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

bool compare(string a, string b)
{
    if(a+b > b+a)
    {
        return true;
    }
    else
    {
        return false;
    }
}

string solution(vector<int> numbers) {
    string answer = "";
    vector<string> Arr;
    
    for(int i=0; i<numbers.size(); i++)
    {
        Arr.push_back(to_string(numbers[i]));
    }
    
    sort(Arr.begin(), Arr.end(), compare);
    
    for(int i=0; i<numbers.size(); i++)
    {
        answer += Arr[i];
    }
    
    if(Arr[0] == "0")
    {
        return "0";
    }
    
    return answer;
}
