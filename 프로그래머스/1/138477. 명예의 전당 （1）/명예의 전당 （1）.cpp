#include <queue>
#include <algorithm>
#include <vector>

using namespace std;

vector<int> solution(int k, vector<int> score) {
    vector<int> answer;
    vector<int> temp;
    
    for (int s : score) {
        temp.push_back(s);
        sort(temp.begin(), temp.end(), greater<int>());
        
        if (temp.size() > k) {
            temp.pop_back();
        }
        answer.push_back(temp.back());
    }
    return answer;
}