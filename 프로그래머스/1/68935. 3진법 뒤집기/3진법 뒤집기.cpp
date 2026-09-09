#include <string>
#include <vector>

using namespace std;

int solution(int n) {
    string str1 = "";
    
    while(n > 0) {
        str1 += to_string(n % 3);
        n /= 3;
    }
    return stoi(str1, nullptr, 3);
}