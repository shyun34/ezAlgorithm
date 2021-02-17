//
//  main.cpp
//  WEEK2_1
//  프로그래머스(LV2.최댓값최솟값)
//  Created by 장병윤 on 2021/02/14.
//

#include <string>
#include <vector>
#include <algorithm>

using namespace std;


bool cal(string a, string b)
{
    int numA = stoi(a);
    int numB = stoi(b);
    
    if(numA <= numB)
    {
        return true;
    }
    else
    {
        return false;
    }
}   


string solution(string s) {
    string answer = "";
    string temp;
    vector<string> v;
        
    for(int i=0; i < s.size(); i++)
    {
        if(s[i] == ' ')
        {
            v.push_back(temp);
            temp = "";
            continue;
        }
        else
        {
            temp += s[i];
        }
    }
    
    v.push_back(temp);
    
    sort(v.begin(), v.end(), cal);
    
    answer = v[0] + " " + v[v.size()-1];
    
    return answer;
}
