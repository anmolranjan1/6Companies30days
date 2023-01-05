#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    string getHint(string &s, string &g)
    {
        int bull = 0;
        int cow = 0;
        unordered_map<char, int> mps;
        unordered_map<char, int> mpg;
        for (int i = 0; i < s.size(); i++)
        {
            if (s[i] == g[i])
            {
                bull++;
            }
            else
            {
                mps[s[i]]++;
                mpg[g[i]]++;
            }
        }

        for (auto a : mpg)
        {
            if (mps.find(a.first) != mps.end())
            {
                // cout<<a.second<<" "<<mps[a.first]<<endl;
                cow += min(a.second, mps[a.first]);
            }
        }
        // cout<<bull<<" "<<cow<<endl;
        string ans = "";
        ans += to_string(bull);
        ans += "A";
        ans += to_string(cow) + "B";
        return ans;
    }
};

int main()
{
    cout << "1 <= secret.length, guess.length <= 1000\nsecret.length == guess.length\nsecret and guess consist of digits only." << endl;
    Solution obj;
    cout << "Enter Secret && guess string:- ";
    string s, g;
    cin >> s >> g;
    cout << obj.getHint(s, g) << endl;
}