#include <bits/stdc++.h>

using namespace std;

int solution(vector<vector<string>> clothes) {
    unordered_map <string, int> ctg_counts;
    
    for(const auto& item : clothes) {
        string ctg = item[1];
        ctg_counts[ctg]++;
    }
    
    int answer = 1;
    
    for(const auto& pair : ctg_counts) {
        answer *= (pair.second + 1);
    }
    
    return answer - 1;
}