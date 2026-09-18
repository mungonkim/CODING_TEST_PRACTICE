#include <string>
#include <bits/stdc++.h>

using namespace std;

vector<int> solution(int n, vector<string> words) {
    unordered_set<string> temp;
    temp.insert(words[0]);
    
    for(int i = 1; i < words.size(); i++) {
        if (words[i].front() != words[i-1].back() || temp.count(words[i])) {
            return {(i%n)+1, (i/n)+1};
        }
        temp.insert(words[i]);
    }

    return {0,0};
}