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
        priority_queue<int, vector<int>, greater<int>> q;
        for (auto a : nums)
        {
            q.push(a);
        }
        int i = 0;
        // cout<<gcd<<endl;
        while (!q.empty())
        {
            // cout<< q.top()<<" ";
            i++;
            if (gcd % (q.top()) == 0)
            {
                i--;
                break;
            }
            q.pop();
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
