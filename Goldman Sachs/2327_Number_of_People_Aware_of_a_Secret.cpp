#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
long long mod=( long long )1e9+7;
    int peopleAwareOfSecret(int n, int delay, int forget) {
        vector<long long> dp(n+1);
        // dp[0]=0;
        dp[1]=1;
        long long peopleNSecret=0;

        for(int i=2;i<=n;i++){
            //number of new people knows the secret on ith day;
             long long  newPeopleSecret=dp[max(i-delay,0)];
             long long  forgetpleople=dp[max(i-forget,0)];
            peopleNSecret=((peopleNSecret+newPeopleSecret)%mod-forgetpleople+mod)%mod;
            dp[i]=(peopleNSecret)%mod;
        }

        long long ans=0;
        for(int i=n-forget+1;i<=n;i++){
            ans=((ans+dp[i])%mod);
        }

        return (int)ans;
    }
};
