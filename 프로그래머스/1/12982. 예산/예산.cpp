#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int solution(vector<int> d, int budget) {
    int answer = 0;
    
    sort(d.begin(), d.end());
    
    for(int n : d) {
        if (n <= budget) {
            answer += 1;
            budget -= n;
        }
        else {
            break;
        }
    }
    return answer;
}