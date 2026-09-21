#include <string>
#include <map>
#include <vector>

using namespace std;

int solution(vector<string> want, vector<int> number, vector<string> discount) {
    int answer = 0;
    map<string, int> wantMap;
    
    for(int i = 0; i < want.size(); i++) {
        wantMap[want[i]] = number[i];
    }
    
    for(int i = 0; i <= discount.size()-10; i++) {
        map<string, int> discountMap;
        
        for(int j = i; j < i+10; j++) {
            discountMap[discount[j]]++;
        }
        
        if(wantMap == discountMap) {
            answer ++;
        }
    }
    return answer;
}