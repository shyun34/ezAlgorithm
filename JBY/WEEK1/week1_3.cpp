//
//  main.cpp
//  WEEK1_3
//  No.10828
//  Created by 장병윤 on 2021/02/02.
//

#include <iostream>
#include <stack>

int n;
int m_num;

std::string m;
std::stack<int> st;

int main(int argc, const char * argv[]) {
    
    std::cin >> n;
    
    for(int i=0; i<n; n++)
    {
        std::cin >> m;
        
        if(m == "push")
        {
            std::cin >> m_num;
            st.push(m_num);
        }
        else if(m == "pop")
        {
            if(!st.empty())
            {
                std::cout << st.top();
                std::cout << '\n';
                st.pop();
            }
            else
            {
                std::cout << -1;
                std::cout << '\n';
            }
        }
        else if(m == "size")
        {
            std::cout << st.size();
            std::cout << '\n';
        }
        else if(m == "empty")
        {
            if(st.empty())
            {
                std::cout << 1;
                std::cout << '\n';
            }
            else
            {
                std::cout << 0;
                std::cout << '\n';
            }
        }
        else if(m == "top")
        {
            if(!st.empty())
            {
                std::cout << st.top();
                std::cout << '\n';
            }
            else
            {
                std::cout << -1;
                std::cout << '\n';
            }
        }
    }
    
    
}
