#include <bits/stdc++.h>
using namespace std;
#define ll long long
class Solution
{
public:
    int minOperations(vector<int> &nums, vector<int> &numsDivide)
    {
        int gcd = numsDivide[0];
        for (int i = 1; i < numsDivide.size(); i++)
        {
            gcd = __gcd(gcd, numsDivide[i]);
        }
        cout << gcd;
        sort(nums.begin(), nums.end());
        int i = 0;
        for (; i < nums.size(); i++)
        {
            if (gcd % nums[i] == 0)
            {
                break;
            }
        }
        return i == nums.size() ? -1 : i;
    }
};

int main()
{
    Solution obj;
    cout << "Enter number of element in nums:- ";
    int _num;
    cin >> _num;
    vector<int> nums(_num);
    for (int i = 0; i < _num; i++)
    {
        cin >> nums[i];
    }

    int nd;
    cout << "Enter number of elements of numsDivide :- ";
    cin >> nd;
    vector<int> vecnd(nd);
    for (int i = 0; i < nd; i++)
    {
        cin >> vecnd[i];
    }
    cout << obj.minOperations(nums, vecnd) << endl;
    ;
}
