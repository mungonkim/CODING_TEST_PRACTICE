#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> answer;
    int max_time = (100-progresses[0] + speeds[0] - 1) / speeds[0];
    int cnt = 1;
    for(int i = 1; i < progresses.size(); i++) {
        if ((100-progresses[i] + speeds[i] - 1) / speeds[i] > max_time) {
            max_time = (100-progresses[i] + speeds[i] - 1) / speeds[i];
            answer.push_back(cnt);
            cnt = 1;
        }
        else{
            cnt+=1;
        }
    }
    answer.push_back(cnt);
    return answer;
}