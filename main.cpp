#include <iostream>
#include <string>
#include <sstream>
using namespace std;
struct Node {
    string val="0";
    int left=0;
    int right=0;
};
Node tree[10001];
void inorder(int i) {
    int left=tree[i].left;
    int right=tree[i].right;
    if (tree[i].val=="0") return;
    inorder(left);
    cout<<tree[i].val;
    inorder(right);
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(NULL);
    for (int tc=1;tc<11;tc++) {

        int N;
        cin>>N;
        for (int i=1;i<=N;i++) {
            tree[i]={"",0,0};
        }
        string dummy;
        getline(cin,dummy);
        for (int i=0;i<N;i++) {
            string line;
            getline(cin,line);
            stringstream ss(line);
            int n,left,right;
            string val;
            ss>>n>>val;
            tree[n].val=val;
            if (ss>>left) {
                tree[n].left=left;
            }
            if (ss>>right) {
                tree[n].right=right;
            }
        }
        cout<<"#"<<tc<<" ";
        inorder(1);
        cout<<endl;
    }

    return 0;

}