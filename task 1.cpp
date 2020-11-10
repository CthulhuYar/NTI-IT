#include<bits/stdc++.h>
using namespace std;

int main()
{
    string s,l;
    bool correctivity=true;
    getline(cin,s);
    for (int i=0; i<s.size(); i++)
        {
            if (s[i]=='(')
                l+='(';
            if (s[i]=='{')
                l+='{';
            if (s[i]=='[')
                l+='[';
            if (s[i]==')')
            {
                if (l[l.size()-1]=='(')
                    l.erase(l.size()-1);
                else
                {
                    correctivity=false;
                    i=s.size();
                }
            }
            if (s[i]=='}')
            {
                if (l[l.size()-1]=='{')
                    l.erase(l.size()-1);
                else
                {
                    correctivity=false;
                    i=s.size();
                }
            }
            if (s[i]==']')
            {
                if (l[l.size()-1]=='[')
                    l.erase(l.size()-1);
                else
                {
                    correctivity=false;
                    i=s.size();
                }
            }
        }
    if ((correctivity==true)&&(l.size()==0))
        cout<<"correct";
    else
        cout<<"incorrect";
}
