#include<bits/stdc++.h>
using namespace std;

int main()
{
    int N,M,nechet=0;
    cin>>N>>M;
    vector <int> counts(N,0);
    for (int i=0; i<M; i++)
    {
       int a,b;
       cin>>a>>b;
       counts[a-1]++;
       counts[b-1]++;
    }
    for (int i=0; i<N; i++)
    {
       if(counts[i]%2==1)
        nechet++;
    }
    if ((nechet==2)||(nechet==0))
        cout<<"Yes";
    else
        cout<<"No";
}
