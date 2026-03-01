#include <deque>
#include <iostream>
#include <vector>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(NULL);
    int N,K;
    cin>>N>>K;
    deque<int> A;
    deque<bool> robot;
    for (int i=0; i<2*N; i++) {
        int a;
        cin>>a;
        A.push_back(a);
        robot.push_back(false);
    }
    int step=0;
    int zero_cnt=0;

    while (true) {
        step++;
        A.push_front(A.back());
        robot.push_front(robot.back());
        A.pop_back();
        robot.pop_back();

        robot[N-1]=false;
        for (int i=N-2;i>=0;i--) {
            if (robot[i]) {
                if (!robot[i+1]&&A[i+1]>=1) {
                    robot[i+1]=true;
                    robot[i]=false;
                    A[i+1]--;
                    if (A[i+1]==0) zero_cnt++;
                }
            }
        }
        robot[N-1]=false;

        if (A[0]>0) {
            robot[0]=true;
            A[0]--;
            if (A[0]==0) zero_cnt++;
        }
        if (zero_cnt>=K) break;
    }
    cout<<step<<"\n";
    return 0;
}