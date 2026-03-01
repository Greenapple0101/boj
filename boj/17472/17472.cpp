#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <utility>

using namespace std;

int N, M;
vector<vector<int>> v;
vector<pair<int, int>> island[7];
vector<vector<int>> visited;
int cnt = 0;
int parent[7]; // Union-Find용 부모 배열

struct Edge {
    int u, v, dist;
    bool operator<(const Edge& other) const {
        return dist < other.dist;
    }
};

// --- Union-Find 함수 ---
int find_root(int x) {
    if (parent[x] == x) return x;
    return parent[x] = find_root(parent[x]);
}

bool unite(int a, int b) {
    a = find_root(a);
    b = find_root(b);
    if (a != b) {
        parent[a] = b;
        return true;
    }
    return false;
}

// --- 섬 정보 저장 (BFS) ---
void bfs(int i, int j, int n) {
    queue<pair<int, int>> q;
    q.push({i, j});
    island[n].push_back({i, j});
    visited[i][j] = 1;
    v[i][j] = n + 1; // 맵에 섬 번호 마킹 (1부터 시작)

    int dy[4] = {0, 0, -1, 1}, dx[4] = {1, -1, 0, 0};
    while (!q.empty()) {
        int y = q.front().first;
        int x = q.front().second;
        q.pop();
        for (int k = 0; k < 4; k++) {
            int ny = y + dy[k], nx = x + dx[k];
            if (ny >= 0 && ny < N && nx >= 0 && nx < M && !visited[ny][nx] && v[ny][nx] == 1) {
                visited[ny][nx] = 1;
                v[ny][nx] = n + 1;
                island[n].push_back({ny, nx});
                q.push({ny, nx});
            }
        }
    }
}

// --- 섬 간의 최단 다리 길이 재기 (직선 전진) ---
int get_dist(int start, int end) {
    int min_len = 1e9;
    int dy[4] = {0, 0, -1, 1}, dx[4] = {1, -1, 0, 0};
    int target_id = end + 1;

    for (auto& pos : island[start]) {
        for (int k = 0; k < 4; k++) {
            int cur_y = pos.first;
            int cur_x = pos.second;
            int len = 0;

            while (true) {
                cur_y += dy[k];
                cur_x += dx[k];

                if (cur_y < 0 || cur_y >= N || cur_x < 0 || cur_x >= M) break;

                if (v[cur_y][cur_x] != 0) {
                    if (v[cur_y][cur_x] == target_id) {
                        if (len >= 2) min_len = min(min_len, len);
                    }
                    break; // 다른 섬(또는 내 섬)에 부딪히면 종료
                }
                len++;
            }
        }
    }
    return min_len;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> N >> M;
    v.assign(N, vector<int>(M));
    visited.assign(N, vector<int>(M, 0));

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            cin >> v[i][j];
        }
    }

    // 1. 섬 분리 및 번호 매기기
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            if (v[i][j] == 1 && !visited[i][j]) {
                bfs(i, j, cnt);
                cnt++;
            }
        }
    }

    // 2. 모든 섬 쌍에 대해 건설 가능한 다리 찾기
    vector<Edge> edges;
    for (int i = 0; i < cnt; i++) {
        for (int j = i + 1; j < cnt; j++) {
            int d = get_dist(i, j);
            if (d != 1e9) {
                edges.push_back({i, j, d});
            }
        }
    }

    // 3. 크루스칼 알고리즘을 이용한 MST 구하기
    sort(edges.begin(), edges.end());
    for (int i = 0; i < cnt; i++) parent[i] = i;

    int total_dist = 0;
    int bridge_count = 0;

    for (auto& edge : edges) {
        if (unite(edge.u, edge.v)) {
            total_dist += edge.dist;
            bridge_count++;
        }
    }

    // 4. 모든 섬이 연결되었는지 확인 (간선 수 = 노드 수 - 1)
    if (bridge_count == cnt - 1 && cnt > 0) {
        cout << total_dist << "\n";
    } else {
        cout << -1 << "\n";
    }

    return 0;
}