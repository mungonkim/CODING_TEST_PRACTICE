#include <string>
#include <iostream>
#include <vector>

using namespace std;

vector<int> solution(int brown, int yellow) {
    int n = brown + yellow;
    for(int i = 1; i <= n; i++) {
        if (n % i == 0) {
            int w = i;
            int h = n / i;
            
            if(w >= h && (w-2) * (h-2) == yellow) {
                return {w, h};
            }
        }
    }
}