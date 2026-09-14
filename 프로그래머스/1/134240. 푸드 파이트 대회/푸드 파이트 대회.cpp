#include <string>
#include <algorithm>
#include <vector>
using namespace std;

string solution(vector<int> food) {
    string left = "";
    
    for(int i = 1; i < food.size(); i++) {
        left += string(food[i] / 2, i + '0');
    }
    
    string right = left;
    reverse(right.begin(), right.end());
    
    return left + '0' + right;
}