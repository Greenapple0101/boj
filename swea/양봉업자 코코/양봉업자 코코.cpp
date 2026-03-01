#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int N,M;
vector<vector<int>> honey;
vector<vector<int>> visited;
int T;
//첫번째가 짝수
//두번째가 헐수
int di[2][6]={
    {0,0,-1,-1,-1,1},
    {0,0,1,1,1,-1}
};
int dj[2][6]={
    {1,-1,0,-1,1,0},
    {1,-1,1,0,-1,0}
};


int dfs(int level, int i, int j) {
    if (level==3) {
        return 0;
    }
    int res=0;
    int type=j%2;
    for (int k=0;k<6;k++) {
        int ni=i+di[type][k];
        int nj=j+dj[type][k];
        if (ni >= 0 && ni < N && nj >= 0 && nj < M && !visited[ni][nj]) {
            visited[ni][nj]=1;
            res=max(res,honey[ni][nj]+dfs(level+1,ni,nj));
            visited[ni][nj]=0;
        }
    }
    return res;
}

int dii[2][3]={
    {-1,0,-1},
    {1,0,1}
};
int djj[2][3]={
    {1,0,-1},
    {1,0,-1}
};

int special(int i,int j) {
    int res=honey[i][j];
    int res2=honey[i][j];
    int type=j%2;
    vector<int> neighbors;
    for (int k=0;k<6;k++) {
        int ni=i+di[type][k];
        int nj=j+dj[type][k];
        if (ni >= 0 && ni < N && nj >= 0 && nj < M && !visited[ni][nj]) {
            neighbors.push_back(honey[ni][nj]);
        }
    }
    sort(neighbors.rbegin(),neighbors.rend());

    return honey[i][j]+neighbors[0]+neighbors[1]+neighbors[2];
}

int main() {
    int T;
    cin>>T;
    for (int tc=1;tc<=T;tc++) {
        cin>>N>>M;
        honey.assign(N,vector<int>(M));
        visited.assign(N,vector<int>(M,0));
        for (int i=0;i<N;i++) {
            for (int j=0;j<M;j++) {
                cin>>honey[i][j];
            }
        }
        int maxy=0;
        for (int i=0;i<N;i++) {
            for (int j=0;j<M;j++) {
                visited[i][j] = 1;
                maxy=max(maxy,honey[i][j]+dfs(0,i,j));
                maxy=max(maxy,special(i,j));
                visited[i][j] = 0;
            }
        }
        cout<<"#"<<tc<<" "<<maxy<<endl;
    }


    return 0;
}