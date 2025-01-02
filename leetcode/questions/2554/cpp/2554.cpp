#include <vector>
#include <set>

class Solution {
public:
    int maxCount(std::vector<int>& banned, int n, int maxSum) {
        std::set<int> setBanned;
        int curSum = 0;
        int cnt = 0;

        for (int num: banned) {
            if (num <= n) {
                setBanned.insert(num);
            }
        }

        for (int num = 1; num <= n && num + curSum <= maxSum; ++num) {
            if (setBanned.find(num) == setBanned.end()) {
                curSum += num;
                cnt += 1;
            }
        }

        return cnt;
    }
};