#include <algorithm>
#include <vector>
#include <unordered_map>

using namespace std;

int solution(int k, vector<int> tangerine) {
    unordered_map<int, int> counts;
    
    for (int t : tangerine) {
        counts[t]++;
    }
    
    vector<int> freqs;
    for (const auto& pair:counts) {
        freqs.push_back(pair.second);
    }
    
    sort(freqs.begin(), freqs.end(), greater<int>());
    
    int answer = 0;
    
    for (int f : freqs) {
        k -= f;
        answer++;
        if (k <= 0) break;
    }
    return answer;
}