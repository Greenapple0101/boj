#include <iostream>
#include <vector>
#include <algorithm> // abs, min 함수 사용

using namespace std;

// 전역 변수로 관리 (solve 안에서 초기화 필수)
int miny;
int total;
bool visited[11]; // 중복 방문(무한 루프) 방지용

int dfs(int i, vector<int> adj[], int clue[]) {
    visited[i] = true; // 현재 마을 방문 도장 찍기
    int sum = clue[i]; // 내 마을 인구수로 시작

    for (int val : adj[i]) {
        if (!visited[val]) { // 아직 안 가본 연결된 마을만 방문
            sum += dfs(val, adj, clue); // 자식 마을들의 합을 내 sum에 더함
        }
    }

    // 이 지점에서 내 아래 식구들을 한 팀으로 했을 때의 차이 계산
    int diff = abs(total - 2 * sum);
    if (diff < miny) miny = diff;

    return sum; // 부모 마을에게 내 팀의 총합을 보고
}

void solve(int tc) {
    int N;
    if (!(cin >> N)) return;

    // 초기화 (매 케이스마다 반드시!)
    miny = 1e9;
    total = 0;
    vector<int> adj[11];
    int clue[11] = {0};

    // 1. 인접 행렬 입력받아 리스트로 저장
    for (int i = 1; i <= N; i++) {
        for (int j = 1; j <= N; j++) {
            int edge; cin >> edge;
            if (edge == 1) adj[i].push_back(j);
        }
    }

    // 2. 유권자 수 입력 및 전체 합(total) 계산
    for (int i = 1; i <= N; i++) {
        cin >> clue[i];
        total += clue[i];
    }

    // 3. 방문 배열 초기화 후 DFS 시작
    for (int i = 1; i <= N; i++) visited[i] = false;

    dfs(1, adj, clue);

    cout << "#" << tc << " " << miny << endl;
}

int main() {
    int T;
    cin >> T;
    for (int tc = 1; tc <= T; tc++) {
        solve(tc);
    }
    return 0;
}