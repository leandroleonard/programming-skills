#include<bits/stdc++.h>

using namespace std;

int main()
{
    int n, k, e = 100; cin >> n >> k;
    vector<int> c(n);

    for(auto &i: c) cin >> i;

    int index = k; e--;
    if(index>=n) index = n - index;
    if(c[index] == 1) e-=2;

    while(index != 0){
        index = (index + k) % n;
        if(index>=n) index = n - index;
        if(c[index] == 0) e--;
        else e-=3;
    }

    cout << e << endl;

    return 0;
}