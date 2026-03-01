#include <iostream>
#include <vector>
#include <queue>
#include <utility>
using namespace std;
vector<vector<int>> population;
vector<vector<int>> population2;
vector<vector<int>> visited;
int N, L,R;
int satisfy=0;
int ans=0;
bool bfs(int i, int j,int N) {
    vector<pair<int,int>> check;
    int sum=population[i][j], cnt=1;
    visited[i][j]=1;
    check.push_back({i,j});
    queue<pair<int,int>> q;
    q.push({i,j});
    while (!q.empty()){
        int ci=q.front().first;
        int cj=q.front().second;
        int di[4]={0,0,-1,1};
        int dj[4]={1,-1,0,0};
        q.pop();
        for (int k=0;k<4;k++) {
            int ni=ci+di[k];
            int nj=cj+dj[k];
            if (0<=ni && ni<=N-1 && nj<=N-1 && 0<=nj && !visited[ni][nj]) {
                int d=population[ci][cj]-population[ni][nj];
                if (abs(d)<=R && L<=abs(d)) {
                    q.push({ni,nj});
                    visited[ni][nj]=1;
                    cnt++;
                    sum+=population[ni][nj];
                    check.push_back({ni,nj});
                }
            }
        }
    }

    for (int i=0; i<check.size();i++) {
        int y=check[i].first;
        int x=check[i].second;
        population[y][x]=sum/cnt;
    }
    if (cnt>1) {
        return true;
    }
    else return false;
}


int main() {
    ios::sync_with_stdio(0);
    cin.tie(NULL);
    cin >> N >> L >> R;
    population.assign(N, vector<int>(N));
    population2.assign(N, vector<int>(N));
    visited.assign(N,vector<int>(N,0));
    for(int i=0; i<N; i++) {
        for(int j=0; j<N; j++) {
            int a;
            cin>>a;
            population[i][j]=a;
        }
    }
    while (true) {
        bool is_moved =false;
        visited.assign(N,vector<int>(N,0)); //날마다 갱신
        //방문안한 점 기준으로 bfs 돌리기
        for (int i=0; i<N;i++) {
            for (int j=0;j<N;j++) {
                if (!visited[i][j]) {
                    if (bfs(i,j,N)) is_moved =true;
                }
            }
        }
        if (!is_moved) break;
        ans++;
    }


    cout<<ans;

    return 0;
}