#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    string longestPrefix(string s)
    {
        int n = s.size();
        vector<int> pi(n, 0);
        for (int i = 1; i < n; i++)
        {
            int j = pi[i - 1];
            while (j > 0 && s[i] != s[j])
            {
                j = pi[j - 1];
            }
            if (s[i] == s[j])
            {
                j++;
            }
            pi[i] = j;
        }

        return s.substr(0, pi[n - 1]);
    }
};

int main()
{
    Solution obj;
    string str;
    cout << "Enter the string:- ";
    cin >> str;
    cout << obj.longestPrefix(str) << endl;
}