/*
 * @Description: 
 * @LastEditors: liukai
 * @Date: 2020-05-15 21:20:51
 * @LastEditTime: 2020-05-15 21:24:27
 * @FilePath: /pyFile/圆圆的py/creat_input.cpp
 */ 
#include <iostream>
using namespace std;

int main() {
    for(int i = 1;i <= 10; i++) {
        for(int j = 0; j < 4; j++) {
            std::cout << i << " ";
        }
        std::cout << std::endl;
    }
    return 0;
}