#include <iostream>
#include <algorithm>

using namespace std;

struct Edge{
    int A,B,C;
    bool operator<(const Edge& other) const {
        return C<other.C;
    }
};

int root[10001];
int froot(int x) {
    if (root[x]==x) return x;
    return root[x]=froot(root[x]);
}

void unionn(int a, int b){
    a=froot(a);
    b=froot(b);
    if (a!=b) root[a]=b;
}

int main() {
    ios::sync_with_stdio(false);

    int V, E;
    cin >> V >> E;
    vector<Edge> edges(10001);
    for(int i = 1; i <= E; i++) {
        int A, B, C;
        cin >> A >> B >> C;
        edges[i]={A,B,C};
    }
    sort(edges.begin(),edges.end());
    for (int i=0;i<=V;i++) {
        root[i]=i;
    }
    int ans=0, cnt=0;
    for (auto &e:edges) {
        if (froot(e.A)!=froot(e.B)) {
            unionn(e.A,e.B);
            ans+=e.C;
            if (++cnt==V-1) break;
        }
    }
    cout<<ans;
    return 0;
}