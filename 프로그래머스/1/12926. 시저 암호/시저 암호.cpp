#include <string>
#include <vector>

using namespace std;

string solution(string s, int n) {
    string answer = "";
    for (char c : s) {
        if (c == ' ') {
            answer += ' ';
        } else if (isupper(c)) {
            answer += (c - 'A' + n) % 26 + 'A';
        } else if (islower(c)) {
            answer += (c - 'a' + n) % 26 + 'a';
        }
    }
    return answer;
}