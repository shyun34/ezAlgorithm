//
//  main.cpp
//  WEEK1_2
//  No.2750
//  Created by 장병윤 on 2021/01/31.
//

#include <iostream>

int main(int argc, const char * argv[]) {

    int array[1000];
    int num, i, j, min, index = 0, tmp;
    
    std::cin >> num;
    
    for(int i=0; i<num; i++)
    {
        std::cin >> array[i];
    }
    for(i=0; i<num; i++)
    {
        min = 1000;
        for(j = i; j < num; j++)
        {
            if(min > array[j])
            {
                min = array[j];
                index = j;
            }
        }
        tmp = array[i];
        array[i] = array[index];
        array[index] = tmp;
    }
    for(i = 0; i < num; i++)
    {
        std::cout << array[i] << '\n';
    }
}
