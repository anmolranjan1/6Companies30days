#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    int evalRPN(vector<string> &tokens)
    {
        stack<int> traverse;

        for (string &a : tokens)
        {
            if (a == "/" || a == "-" || a == "*" || a == "+")
            {
                int sec = traverse.top();
                traverse.pop();
                int first = traverse.top();
                traverse.pop();
                long long temp;
                if (a == "+")
                {
                    temp = first + sec;
                }
                else if (a == "-")
                {
                    temp = first - sec;
                }
                else if (a == "*")
                {
                    temp = (long long)first * (long long)sec;
                }
                else
                {
                    temp = first / sec;
                }
                traverse.push((int)temp);
            }
            else
            {
                if (a[0] == '-')
                {
                    string temp = a.substr(1);
                    int val = stoi(temp);
                    traverse.push(-val);
                }
                else
                {
                    traverse.push(stoi(a));
                }
            }
        }

        return traverse.top();
    }
};

int main()
{
    Solution obj;
    vector<string> expression = {"10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"};
    cout << obj.evalRPN(expression) << endl;
}