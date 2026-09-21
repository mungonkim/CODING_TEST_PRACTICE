#include <bits/stdc++.h>

using namespace std;
bool isValid(string s) {
    stack<char> st;
    
    for(char c : s) {
        if (c == '(' || c == '{' || c == '[') {
            st.push(c);
        } else {
            if (st.empty()) return false;
            
            char top = st.top();
            if ((c == ')' && top == '(') ||
                (c == '}' && top == '{') ||
                (c == ']' && top == '[')) {
                st.pop();
            } else {
                return false;
            }
        }
    }
    return st.empty();
}
int solution(string s) {
    int answer = 0;
    int len = s.length();
    
    for(int x = 0; x < len; x++) {
        string rotated = s.substr(x) + s.substr(0, x);
        
        if (isValid(rotated)) {
            answer++;
        }
    }
    return answer;
}