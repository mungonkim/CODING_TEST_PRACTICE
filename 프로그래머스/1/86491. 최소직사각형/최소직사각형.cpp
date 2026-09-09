#include <string>
#include <vector>

using namespace std;

int solution(vector<vector<int>> sizes) {
    int w_max = 0;
    int h_max = 0;
    
    for(auto card : sizes) {
        int w = max(card[0], card[1]);
        int h = min(card[0], card[1]);
        
        w_max = max(w_max, w);
        h_max = max(h_max, h);
    }
    return w_max * h_max;
}