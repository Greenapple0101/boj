#include <iostream>
#include <vector>
#include <queue>

using namespace std;

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
    return 0;
}