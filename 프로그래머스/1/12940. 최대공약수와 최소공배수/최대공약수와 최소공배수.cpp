#include <string>
#include <vector>
#include <numeric>

using namespace std;

vector<int> solution(int n, int m) {

    int gcd_val = gcd(n, m);
    int lcm_val = lcm(n, m);
    
    
    return {gcd_val, lcm_val};
}