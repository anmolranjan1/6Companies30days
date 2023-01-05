#include <bits/stdc++.h>
using namespace std;

class Solution
{
    vector<int> num = {1, 2, 3, 4, 5, 6, 7, 8, 9};
    vector<vector<int>> ans;
    void func(int i, int &k, int &n, vector<int> &temp, int sum)
    {
        if (sum == n)
        {
            if (temp.size() == k)
            {
                ans.push_back(temp);
            }
            return;
        }
        if (i >= 9)
        {
            return;
        }
        sum += num[i];
        temp.push_back(num[i]);
        func(i + 1, k, n, temp, sum);
        sum -= temp[temp.size() - 1];
        temp.pop_back();
        func(i + 1, k, n, temp, sum);
    }

public:
    vector<vector<int>> combinationSum3(int k, int n)
    {
        vector<int> temp;
        func(0, k, n, temp, 0);
        return ans;
    }
};

int main()
{
    Solution obj;
    int n;
    cout << "2 <= k <= 9    1 <= n <= 60" << endl;
    cout << "Enter n:";
    cin >> n;
    int k;
    cout << "Enter k:";
    cin >> k;

    vector<vector<int>> sol = obj.combinationSum3(k, n);

    for (auto a : sol)
    {
        for (auto b : a)
        {
            cout << b << " ";
        }
        cout << endl;
    }
}