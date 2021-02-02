//
//  main.cpp
//  WEEK1_1
//  No.1158
//  Created by 장병윤 on 2021/01/31.
//

#include <iostream>
#include <queue>

int main(int argc, const char * argv[]) {
    
        int n, k;
        int temp;
        std::queue<int> q;
     
        std::cin >> n >> k; // (N,K)
     
        for (int i = 1; i <= n; i++) {
            q.push(i);
        }
     
        std::cout << "<";
    
        while (1) {
            for (int i = 0; i < k - 1; ++i) {
                temp = q.front();
                q.pop();
                q.push(temp);
            }
            std::cout << q.front();
            q.pop();
            if (!q.size()) {
                break;
            }
            std::cout << ", ";
        }
        std::cout << ">";
     
        return 0;
}
