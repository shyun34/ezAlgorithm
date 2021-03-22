//
//  main.cpp
//  WEEK4_2
//  프로그래머스 Lv2 > 행렬의 곱셈
//  Created by 장병윤 on 2021/03/22.
//

#include <string>
#include <vector>

using namespace std;

vector<vector<int>> solution(vector<vector<int>> arr1, vector<vector<int>> arr2) {
    
    vector<vector<int>> answer;
    
    for (int i = 0; i < arr1.size(); i++)
    {
        vector<int> tmp;
        
        for (int j = 0; j < arr2[0].size(); j++)
        {
            int value = 0;
            
            for (int k = 0; k < arr1[0].size(); k++)
            {
                value += arr1[i][k] * arr2[k][j];
                tmp.push_back(value);
            }
        }
        answer.push_back(tmp);
    }
    return answer;
}
