#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    int numberOfSubstrings(string s)
    {
        int vec[3] = {0, 0, 0};
        int j = 0;
        int n = s.size();
        int ans = 0;
        for (int i = 0; i < n; i++)
        {
            vec[s[i] - 'a']++;
            while (vec[0] && vec[1] && vec[2])
            {
                vec[s[j] - 'a']--;
                j++;
            }
            ans += j;
        }

        return ans;
    }
};
int main()
{
    Solution obj;
    cout << "3 <= s.length <= 5 x 10^4\ns only consists of a, b or c characters." << endl;
    string str;
    cout << "Enter String:-";
    cin >> str;
    cout << obj.numberOfSubstrings(str) << endl;
}