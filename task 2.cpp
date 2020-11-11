#include<bits/stdc++.h>
using namespace std;

void dfs(int start, vector<bool>& color, const vector<vector<int>>& G, int n){
    color[start] = true;
    for(int v = 0; v < n; v++){
        if(v != start && G[start][v] == 1 && !color[v])
            dfs(v, color, G, n);
    }
}

int main()
{
    int N,M,nechet=0;
    cin>>N>>M;
    vector <int> counts(N,0);
    vector<bool> color(N, false);
    vector<vector<int>> G(N, vector<int>(N, 0));
    for (int i=0; i<M; i++)
    {
        int a,b;
        cin>>a>>b;
        counts[a-1]++;
        counts[b-1]++;
        G[a - 1][b - 1] = 1;
        G[b - 1][a - 1] = 1;
    }
    for (int i=0; i<N; i++)
    {
        if(counts[i]%2==1)
            nechet++;
    }
    int Ncomp = 0;
    for(int i = 0; i < N; i++){
        if (!color[i]){
            Ncomp++;
            dfs(i, color, G, N);
        }
    }
    if (nechet <= 2 && Ncomp == 1)
        cout<<"Yes";
    else
        cout<<"No";
}
