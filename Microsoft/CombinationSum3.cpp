class Solution
{
public:
    void sum(int i, vector<vector<int>> &ans, vector<int> &nums, vector<int> &v, int tar, int k)
    {
        if (i >= nums.size())
        {
            if (v.size() == k && tar == 0)
            {
                ans.push_back(v);
            }
            return;
        }

        if (nums[i] <= tar)
        {
            v.push_back(nums[i]);
            sum(i + 1, ans, nums, v, tar - nums[i], k);
            v.pop_back();
        }
        sum(i + 1, ans, nums, v, tar, k);
    }

public:
    vector<vector<int>> combinationSum3(int k, int n)
    {
        vector<int> nums;
        vector<vector<int>> ans;
        vector<int> v;

        for (int j = 1; j <= 9; j++)
        {
            nums.push_back(j);
        }
        sum(0, ans, nums, v, n, k);
        return ans;
    }
};