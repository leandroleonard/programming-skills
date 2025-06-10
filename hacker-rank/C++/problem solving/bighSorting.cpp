#include <bits/stdc++.h>

using namespace std;

bool custom(string a, string b){
    if (a.size() == b.size())
        return a < b; 
    return a.size() < b.size();     
}

int main(){
    int n; cin >> n;
    
    vector<string> s(n);
    
    for(int i = 0; i < n; i++) cin >> s[i];
    sort(s.begin(), s.end(), custom);
    
    for(int i =0; i< n; i++) cout << s[i] << endl;
    return 0;
}