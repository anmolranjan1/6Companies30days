#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define pll pair<ll, ll>
class Solution
{
public:
    int MOD = 1e9 + 7;
    int countPaths(int n, vector<vector<int>> &roads)
    {
        vector<vector<pll>> adj(n);
        for (auto &road : roads)
        {
            ll u = road[0], v = road[1], w = road[2];
            adj[u].push_back({v, w});
            adj[v].push_back({u, w});
        }
        return dijkstra(adj, n, 0);
    }
    int dijkstra(const vector<vector<pll>> &adj, int n, int src)
    {
        vector<ll> dist(n, LONG_MAX);
        vector<ll> ways(n);
        ways[src] = 1;
        dist[src] = 0;
        priority_queue<pair<ll, ll>, vector<pair<ll, ll>>, greater<pair<ll, ll>>> q;
        while (!q.empty())
        {
            auto f = q.top();
            q.pop();
            ll d = f.first;
            ll u = f.second;
            if (d > dist[u])
                continue;
            for (auto a : adj[u])
            {
                ll v = a.first;
                ll w = a.second;
                if (dist[v] > d + w)
                {
                    dist[v] = d + w;
                    ways[v] = ways[u];
                    q.push({dist[v], v});
                }
                else if (dist[v] == d + w)
                {
                    ways[v] = (ways[v] + ways[u]) % MOD;
                }
            }
        }
        return ways[n - 1];
    }
};

int main()
{
    Solution obj;
    cout << "Enter number of node:- ";
    int _num;
    cin >> _num;
    vector<vector<int>> vec = {
        {0, 6, 7}, {0, 1, 2}, {1, 2, 3}, {1, 3, 3}, {6, 3, 3}, {3, 5, 1}, {6, 5, 1}, {2, 5, 1}, {0, 4, 5}, {4, 6, 2}};
    cout << obj.countPaths(_num, vec);
}
