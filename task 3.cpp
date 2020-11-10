#include <bits/stdc++.h>

using namespace std;

vector<int> graph[1000];
char color[1000];     //Цвет будем представлять типом char
                        //0 - вершина ещё не покрашена; 1, 2 - различные цвета.

inline char invert(int c) {
    return c == 1 ? 2 : 1;
}

void dfs(int v, char c) {   //c - цвет текущей вершины
    color[v] = c;

    for (int u: graph[v]) {
        if (color[u] == 0) {    //непосещённая вершина
            dfs(u, invert(c));
        } else if (color[u] == c) {
            cout << "bad" << endl;
            exit(0);
        }
    }
}

int main() {
    int n, m;
    cin >> n >> m;

    for (int i = 0; i < m; i++) {
        int u, v;
        cin >> u >> v;
        u--, v--;

        graph[u].push_back(v);
        graph[v].push_back(u);
    }
    for (int i = 0; i < n; i++) {
        if (color[i] == 0) {
            dfs(i, 1);
        }
    }

    cout << "good" << endl;
}
