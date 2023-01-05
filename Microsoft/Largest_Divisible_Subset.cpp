#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    vector<int> largestDivisibleSubset(vector<int> &nums)
    {
        sort(nums.begin(), nums.end());

        int n = nums.size();
        vector<int> dp(n, 1);
        vector<int> prevInd(n);
        int maxi = 1;
        int lastInd = 0;
        for (int i = 0; i < n; i++)
        {
            prevInd[i] = i;
            for (int prev = 0; prev < i; prev++)
            {
                if (nums[i] % nums[prev] == 0 && 1 + dp[prev] > dp[i])
                {
                    dp[i] = 1 + dp[prev];
                    prevInd[i] = prev;
                }
            }

            if (dp[i] > maxi)
            {
                maxi = dp[i];
                lastInd = i;
            }
        }

        vector<int> ans;
        ans.push_back(nums[lastInd]);
        while (prevInd[lastInd] != lastInd)
        {
            lastInd = prevInd[lastInd];
            ans.push_back(nums[lastInd]);
        }

        return ans;
    }
};

int main()
{
    Solution obj;
    cout << "Constraints:\n1 <= nums.length <= 1000\n1 <=nums[i] <= 2 * 109\nAll the integers in nums are unique." << endl;

    int num;
    cout << "Enter Number of element in array:-";
    cin >> num;
    vector<int> vec(num);
    for (int i = 0; i < num; i++)
    {
        cin >> vec[i];
    }

    vector<int> lds = obj.largestDivisibleSubset(vec);

    for (auto a : lds)
        cout << a << " ";
    cout << endl;
}