class Solution
{
public:
    string getHint(string s, string g)
    {
        vector<int> st(10), gt(10);
        int bulls = 0;
        for (int i = 0; i < s.size(); i++)
        {
            if (s[i] == g[i])
            {
                bulls++;
            }
            else
            {
                st[s[i] - '0']++;
                gt[g[i] - '0']++;
            }
        }
        int cow = 0;
        for (int i = 0; i < 10; i++)
            cow += min(st[i], gt[i]);

        string temp = "";
        temp += to_string(bulls);
        temp += "A";
        temp += to_string(cow);
        temp += "B";
        return temp;
    }
};