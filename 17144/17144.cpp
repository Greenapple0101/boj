#include <iostream>
#include <vector>
#include <cmath>
#include <utility>
using namespace std;
int di[4]={0,0,-1,1};
int dj[4]={1,-1,0,0};

void spread(vector<vector<int>> &grid, int R, int C) {
    vector<vector<int>> temp(R,vector<int>(C,0));
    for (int i=0;i<R;i++)
    {for (int j=0;j<C;j++) {
        if (grid[i][j]!=-1&&grid[i][j]!=0) {
            int amount=grid[i][j]/5;
            int cnt=0;
            for (int k=0;k<4;k++) {
                int ni=i+di[k];
                int nj=j+dj[k];
                if (ni>=0 && ni<R && nj>=0 && nj<C && grid[ni][nj]!=-1) {
                    temp[ni][nj]+=amount;
                    cnt++;
                }
            }
            grid[i][j]-=(amount*cnt);
        }
    }
    }
    for (int i=0;i<R;i++) {
        for (int j=0;j<C;j++) {
            if (grid[i][j]!=-1) {
                grid[i][j]+=temp[i][j];
            }
        }
    }
}

void debug(vector<vector<int>> &grid,int R, int C) {
    for (int i=0;i<R;i++) {

        for (int j=0;j<C;j++) {
            cout<<grid[i][j]<<" ";
        }
        cout<<"\n";
    }
}

void airupper(vector<vector<int>> &grid,int R, int C, int up) {
    for (int i=up-1;i>0;i--) grid[i][0]=grid[i-1][0]; //왼쪽벽
    for (int i=0;i<C-1;i++) grid[0][i]=grid[0][i+1]; //위쪽벽
    for (int i=0;i<up;i++) grid[i][C-1]=grid[i+1][C-1]; // 오른쪽 벽
    for (int i=C-1; i>1;i--) grid[up][i]=grid[up][i-1]; // 공기청정기벽
    grid[up][1]=0;
}

void airdown(vector<vector<int>> &grid,int R, int C, int down) {
    for (int i=down+1; i<R-1;i++) grid[i][0]=grid[i+1][0];
    for (int i=0;i<C-1;i++) grid[R-1][i]=grid[R-1][i+1];
    for (int i=R-1;i>down;i--) grid[i][C-1]=grid[i-1][C-1];
    for (int i=C-1;i>1;i--) grid[down][i]=grid[down][i-1];
    grid[down][1]=0;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int R, C, T;
    cin >> R >> C >> T;
    vector<vector<int>> grid(R, vector<int>(C));
    for(int i=0; i<R; i++) {
        for(int j=0; j<C; j++) {
            cin >> grid[i][j];
        }
    }
    vector<pair<int,int>> p;
    for (int i=0;i<R;i++) {
        for (int j=0;j<C;j++) {
            if (grid[i][j]==-1) {
                p.push_back({i,j});
            }
        }
    }
    int up=p[0].first;
    int down=p[1].first;
    while (T--) {
        spread(grid, R, C);
        airupper(grid, R, C, up);
        airdown(grid, R, C, down);
    }
    int sum=0;
    for (int i=0;i<R;i++) {
        for (int j=0;j<C;j++) {
            sum+=grid[i][j];
        }
    }
    cout<<sum+2;
    return 0;
}