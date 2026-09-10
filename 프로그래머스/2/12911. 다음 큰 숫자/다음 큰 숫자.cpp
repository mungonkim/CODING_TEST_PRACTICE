#include <string>
#include <iostream>
#include <vector>

using namespace std;

int solution(int n) {
    int target = __builtin_popcount(n);
    int next_n = n + 1;
    
    while (true) {
        if (__builtin_popcount(next_n) == target) {
            return next_n;
        }
        next_n++;
    }
}