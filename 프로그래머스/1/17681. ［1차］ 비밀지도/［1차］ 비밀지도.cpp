#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

vector<string> solution(int n, vector<int> arr1, vector<int> arr2) {
    vector<string> answer;
    
    for(int i = 0; i < n; i++) {
        string row1 = "";
        string row2 = "";
        
        while (arr1[i] != 0) {
            row1 += to_string(arr1[i] % 2);
            arr1[i] = arr1[i] / 2;
        }
        
        while (arr2[i] != 0) {
            row2 += to_string(arr2[i] % 2);
            arr2[i] = arr2[i] / 2;
        }
        
        while (row1.size() < n) row1 += '0';
        while (row2.size() < n) row2 += '0';
        
        reverse(row1.begin(), row1.end());
        reverse(row2.begin(), row2.end());
        
        string temp = "";
        
        for(int j = 0; j < row1.size(); j++) {
            if (row1[j] == '1' || row2[j] == '1') {
                temp += '#';
            }
            else {
                temp += ' ';
            }
        }
        answer.push_back(temp);
    }
    return answer;
}