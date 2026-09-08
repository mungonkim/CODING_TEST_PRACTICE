#include <string>
#include <vector>
#include <algorithm>
using namespace std;

vector<int> solution(string s) {
    int change_count = 0; // 변환 결과
    int removed_zero = 0; // 제거된 0의 횟수
    
    while (s != "1") {
        int ones = 0;
    
        for(char c : s) { 
            if (c == '1') ones++;
        }
    
        removed_zero += (s.size()-ones);
        
        // 1개수 2진 변환 
        int c = ones;
        string next_s = "";
        while (c > 0) {
            next_s += to_string(c%2);
            c /= 2;
        }
    
        reverse(next_s.begin(), next_s.end());
    
        s = next_s;
        change_count++;
    }
    return {change_count, removed_zero};
}