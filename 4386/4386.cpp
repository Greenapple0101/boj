#include <cmath>
#include <vector>
#include <iostream>
#include <algorithm>
#include <iomanip>
using namespace std;
int rootty[101];

struct Edge {
    int x;
    int y;
    double dist;
    bool operator< (const Edge& other) const{
        return dist<other.dist;
    }
};

int rot(int x) {
    if (rootty[x]==x) return x;
    return rootty[x]=rot(rootty[x]);
}

void unite(int a, int b) {
    a=rot(a);
    b=rot(b);
    if (a!=b) {
        rootty[a]=b;
    }
}


int main() {
    ios::sync_with_stdio(false);

    int n;
    cin >> n;

    vector<pair<double, double>> stars;
    for (int i = 0; i < n; ++i) {
        double x, y;
        cin >> x >> y;
        stars.push_back({x, y});
    }
    vector<Edge> edges;
    for (int i=0;i<n;i++)
        for (int j=0;j<n;j++) {
            double dist=hypot(stars[i].first-stars[j].first,stars[i].second-stars[j].second);
            edges.push_back({i,j,dist});
        }

    sort(edges.begin(),edges.end());
    double ans=0;
    int cnt=0;
    for (int i=0;i<n;i++) {
        rootty[i]=i;
    }
    for (auto& val:edges) {
        if (rot(val.x)!=rot(val.y)) {
            unite(val.x,val.y);
            ans+=val.dist;
            if (++cnt==n-1) break;
        }
    }
    cout<<fixed<<setprecision(2)<<ans;
    return 0;
}