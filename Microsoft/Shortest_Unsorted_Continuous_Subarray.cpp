#include <bits/stdc++.h>
using namespace std;

class SolutionNlogN
{
public:
    int findUnsortedSubarray1(vector<int> &nums)
    {
        vector<int> temp(nums.begin(), nums.end());
        sort(temp.begin(), temp.end());
        int i;
        for (i = 0; i < nums.size(); i++)
        {
            if (nums[i] != temp[i])
            {
                break;
            }
        }
        int j = nums.size() - 1;
        for (; j >= 0; j--)
        {
            if (nums[j] != temp[j])
                break;
        }
        if (i < nums.size() && j >= 0)
            return j - i + 1;

        return 0;
    }
};

class SolutionO_N
{
public:
    int findUnsortedSubarray(vector<int> &nums)
    {
        int end = -1;
        int maxi = nums[0];
        for (int i = 1; i < nums.size(); i++)
        {
            if (maxi > nums[i])
            {
                end = i;
            }
            else
            {
                maxi = max(maxi, nums[i]);
            }
        }

        int start = 0;
        int mini = nums[nums.size() - 1];
        for (int i = nums.size() - 2; i >= 0; i--)
        {
            if (nums[i] > mini)
            {
                start = i;
            }
            else
            {
                mini = min(mini, nums[i]);
            }
        }

        return (end - start + 1 >= 0 ? end - start + 1 : 0);
    }
};

int main()
{
    SolutionO_N obj;
    cout << "Constraints:\n1 <= nums.length <= 104\n-105 <= nums[i] <= 105" << endl;

    int num;
    cout << "Enter Number of element in array:-";
    cin >> num;
    vector<int> vec(num);
    for (int i = 0; i < num; i++)
    {
        cin >> vec[i];
    }
    SolutionNlogN obj1;
    cout << "NlogN " << obj1.findUnsortedSubarray1(vec) << endl;

    cout << "O(N) " << obj.findUnsortedSubarray(vec) << endl;
    ;
}