#include <iostream>
#include <vector>
#include <algorithm>
#include <utility>
using namespace std;
vector<vector<int>> grid;
vector<vector<bool>> eaten;
bool check(int poi,int poj, int soli, int solj) {
    if (poi==soli) {
        if (solj<poj) {
            int count=0;
            for (int i=solj+1;i<poj;i++) {
                if (grid[poi][i]==1) count++;
            }
            if (count==1) return true;
        }
        else if (solj>poj) {
            int count=0;
            for (int i=poj+1;i<solj;i++) {
                if (grid[poi][i]==1) count++;
            }
            if (count==1) return true;
        }
    }
    if (poj==solj) {
        if (soli<poi) {
            int count=0;
            for (int i=soli+1;i<poi;i++) {
                if (grid[i][poj]==1) count++;
            }
            if (count==1) return true;
        }
        else if (soli>poi) {
            int count=0;
            for (int i=poi+1;i<soli;i++) {
                if (grid[i][poj]==1) count++;
            }
            if (count==1) return true;
        }
    }
    return false;
}
pair<int,int> po;
int N;
int county=0;
int ans;
void dfs(int time,int poi,int poj) {
    if (time==3) {
        return;
    }
    for (int i=0;i<N;i++) {
        for (int j=0;j<N;j++) {
            if (grid[i][j]==1 && check(poi,poj,i,j)) {
                eaten[i][j] = true;
                grid[i][j]=0;
                dfs(time+1,i,j);
                grid[i][j]=1;
            }
            else if (grid[i][j]==0 && check(poi,poj,i,j)) {
                dfs(time+1,i,j);
            }
        }
    }
}


int main() {
    int T;
    cin>>T;
    for (int tc=1;tc<=T;tc++) {
        cin>>N;
        grid.assign(N,vector<int>(N));
        eaten.assign(N,vector<bool>(N,false));
        for (int i=0;i<N;i++) {
            for (int j=0;j<N;j++) {
                cin>>grid[i][j];
            }
        }
        for (int i=0;i<N;i++) {
            for (int j=0;j<N;j++) {
                if (grid[i][j]==2) {
                    po={i,j};
                    grid[i][j]=0;
                }
            }
        }
        int poi=po.first;
        int poj=po.second;
        int ans=0;
        dfs(0,poi,poj);
        for (int i=0;i<N;i++) {
            for (int j=0;j<N;j++) {
                if (eaten[i][j]) {
                    ans++;
                }
            }
        }
        cout<<"#"<<tc<<" "<<ans<<endl;
    }
    return 0;
}