#include <bits/stdc++.h>
using namespace std;

class Solution
{
    void pop_front(vector<int> &v)
    {
        if (v.size() > 0)
        {
            v.erase(v.begin());
        }
    }

public:
    int maxRotateFunction(vector<int> &nums)
    {
        int n = nums.size();
        int maxi = INT_MIN;
        for (int i = 0; i < n; i++)
        {
            int curr = 0;
            for (int j = 0; j < n; j++)
            {
                curr += (j * nums[j]);
            }
            maxi = max(maxi, curr);
            int temp = nums[n - 1];
            nums.pop_back();
            nums.insert(nums.begin(), temp);
        }
        return maxi;
    }
};

int main()
{
    cout << "Constraints:\nn == nums.length\n1 <= n <= 105\n-100 <= nums[i] <= 100" << endl;
    Solution obj;
    int num;
    cout << "Enter num:- ";
    cin >> num;
    vector<int> vec(num);
    cout << "Enter vector:- ";
    for (int i = 0; i < num; i++)
        cin >> vec[i];

    cout << obj.maxRotateFunction(vec) << endl;
}