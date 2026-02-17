#include <queue>
#include <vector>
#include <iostream>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    int N, M;
    cin >> N >> M;
    vector<int> problems[100001];
    vector<int> count(N+1);
    for (int i = 0; i < M; ++i) {
        int A, B;
        cin >> A >> B;
        problems[A].push_back(B);
        count[B]++;
    }
    queue<int> q;
    for (int i=1;i<N+1;i++) {
        if (count[i]==0) {
            q.push(i);
        }
    }
    while (!q.empty()) {
        int curr=q.front();
        cout<<curr<<" ";
        q.pop();
        for (int val:problems[curr]) {
            count[val]--;
            if (count[val]==0) {
                q.push(val);
            }
        }
    }

    return 0;
}