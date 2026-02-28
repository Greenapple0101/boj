#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int T;
int N;
int miny;
int sum;
int maxy;
vector<int> bal;
void dfs(int ssum) {
    if (bal.size()==0){
        maxy=max(maxy,ssum);
    }
    for (int num=0;num<bal.size();num++) {
        if (bal.size()==1) {sum=bal[num];}
        else if (num>0 && num<bal.size()-1)
        {sum=bal[num-1]*bal[num+1];}
        else if (num==0) {
            sum=bal[num+1];
        }
        else if (num==bal.size()-1) {
            sum=bal[num-1];
        }
        int temp=bal[num];
        bal.erase(bal.begin()+num);
        dfs(ssum+sum);
        bal.insert(bal.begin()+num,temp);
    }
}

int main() {
    cin>>T;
    for (int tc=1;tc<=T;tc++) {
        cin>>N;
        bal.assign(N,0);
        for (int i=0;i<N;i++) {
            cin>>bal[i];
        }
        maxy=0;
        dfs(0);
        cout<<"#"<<tc<<" "<<maxy<<endl;
    }
    return 0;
}