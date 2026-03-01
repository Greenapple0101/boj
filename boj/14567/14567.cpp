#include <iostream>
#include <queue>
#include <vector>
#include <utility>
#include <algorithm>
using namespace std;
vector<pair<int,int>> pair1;
int main() {
    ios::sync_with_stdio(false);
    int N, M;
    cin >> N >> M;
    vector<vector<int>> pre(N+1);
    int cnt[1001]={0, };
    for (int i = 0; i < M; ++i) {
        int A, B;
        cin >> A >> B;
        pre[A].push_back(B);
        cnt[B]++;
    }
    queue<int> q;
    for (int i=1;i<N+1;i++) {
        if (cnt[i]==0) {
            q.push(i);
            pair1.push_back({i,1});
        }
    }

    int c=1;
    int semester[1001]={0,};
    while (!q.empty()) {
        int curr=q.front();
        q.pop();
        for (int val:pre[curr]) {
            semester[val]=max(semester[val],semester[curr]+1);
            cnt[val]--;
            if (cnt[val]==0) {
                q.push(val);
            }
        }
    }
    sort(pair1.begin(),pair1.end());
    for (int i=1;i<N+1;i++) {
        cout<<semester[i]+1<<" ";
    }
    return 0;
}