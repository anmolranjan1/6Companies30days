#include <bits/stdc++.h>
using namespace std;

class Solution
{
    void remove(unordered_map<char, int> &mpsize, char ch)
    {
        if (mpsize[ch] == 1)
        {
            mpsize.erase(ch);
        }
        else
        {
            mpsize[ch]--;
        }
    }

public:
    int numberOfSubstrings(string s)
    {
        unordered_map<char, int> mpsize3;
        unordered_map<char, int> mpsize2;
        int ans = 0;
        int i3 = -1;
        int i2 = -1;
        int rel = -1;
        int n = s.size();
        while (true)
        {
            // cout<<i3<<" "<<i2<< " "<<rel<<endl;
            bool flag3 = false, flag2 = false, r = false;
            while (i3 < n - 1)
            {
                // cout<<"i3"<<endl;
                flag3 = true;
                i3++;
                mpsize3[s[i3]]++;
                if (mpsize3.size() == 4)
                {
                    remove(mpsize3, s[i3]);
                    i3--;
                    break;
                }
            }

            while (i2 < i3)
            {
                // cout<<"i2"<<endl;
                flag2 = true;
                i2++;
                mpsize2[s[i2]]++;
                if (mpsize2.size() == 3)
                {
                    remove(mpsize2, s[i2]);
                    i2--;
                    break;
                }
            }

            while (rel < i2)
            {
                // cout<<"rel"<<endl;
                r = true;
                if (mpsize2.size() == 2 && mpsize3.size() == 3)
                {
                    ans += i3 - i2;
                }
                rel++;
                remove(mpsize2, s[rel]);
                remove(mpsize3, s[rel]);
                if (mpsize3.size() < 3 || mpsize2.size() < 2)
                    break;
            }
            if (flag3 == false && flag2 == false && r == false)
                break;
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