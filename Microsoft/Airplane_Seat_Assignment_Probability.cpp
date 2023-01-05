#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    double nthPersonGetsNthSeat(int n)
    {
        return 1 == n ? 1.0 : 0.5;
    }
};
int main()
{
    Solution obj;
    int num;
    cout << "Enter the number of passengers:- ";
    cin >> num;
    cout << obj.nthPersonGetsNthSeat(num) << endl;
}