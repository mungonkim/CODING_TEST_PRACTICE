#include <string>
#include <vector>

using namespace std;

int solution(string t, string p) {
    int answer = 0;
    int p_len = p.size();
    
    long long p_num = stoll(p);
    
    for (int i = 0; i <= (int)t.size()-p_len; i++) {
        string stub = t.substr(i, p_len);
        
        if (stoll(stub) <= p_num) {
            answer++;
        }
    }
    return answer;
}