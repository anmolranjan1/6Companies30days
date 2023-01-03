class Solution
{
public:
    int evalRPN(vector<string> &tokens)
    {
        stack<int> s;
        for (auto x : tokens)
        {
            if (x == "+" || x == "-" || x == "/" || x == "*")
            {
                int op2 = s.top();
                s.pop();
                int op1 = s.top();
                s.pop();

                if (x == "+")
                {
                    s.push(op1 + op2);
                }
                if (x == "-")
                {
                    s.push(op1 - op2);
                }
                if (x == "/")
                {
                    s.push(op1 / op2);
                }
                if (x == "*")
                {
                    s.push(op1 * op2);
                }
            }
            else
            {
                stringstream ss(x);
                int d;
                ss >> d;
                s.push(d);
            }
        }
        return s.top();
    }
};