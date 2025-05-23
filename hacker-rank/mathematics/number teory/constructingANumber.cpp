#include <bits/stdc++.h>
#define ll unsigned long long int

using namespace std;

int main()
{
    int t; cin >> t;
    while(t--){
        int n; cin >> n;
        ll result = 0;
        
        for(int i = 0;i<n;i++){
            ll number; cin >> number;
            result += number;
        }
        
        if(result % 3 == 0) cout << "Yes" << endl;
        else cout << "No" << endl;
        
        
    }
    return 0;
}