#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    bool canFinish(int numCourses, vector<vector<int>> &prerequisites)
    {
        vector<vector<int>> adj(numCourses);
        for (auto a : prerequisites)
        {
            adj[a[0]].push_back(a[1]);
        }
        vector<int> indegree(numCourses, 0);
        for (int i = 0; i < numCourses; i++)
        {
            for (auto a : adj[i])
            {
                indegree[a]++;
            }
        }

        queue<int> q;
        for (int i = 0; i < numCourses; i++)
        {
            if (indegree[i] == 0)
            {
                q.push(i);
            }
        }
        int count = 0;
        while (!q.empty())
        {
            int node = q.front();
            q.pop();
            count++;
            for (auto a : adj[node])
            {
                indegree[a]--;
                if (indegree[a] == 0)
                    q.push(a);
            }
        }

        return count == numCourses;
    }
};

int main()
{
    cout << "Constraints:\n1 <= numCourses <= 2000\n0 <= prerequisites.length <= 5000\nprerequisites[i].length == 2\n0 <= ai, bi < numCourses\nAll the pairs prerequisites[i] are unique." << endl;
    Solution obj;
    int num;
    cout << "Enter numCourses:- ";
    cin >> num;
    cout << "Enter number of prerequisites :- ";
    int prenum;
    cin >> prenum;
    vector<vector<int>> vec(prenum, vector<int>(2));

    for (int i = 0; i < prenum; i++)
        for (int j = 0; j < 2; j++)
            cin >> vec[i][j];
    cout << obj.canFinish(num, vec);
}