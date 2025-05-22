#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n;
    cin >> n;

    vector<int> p(100, 0), ans(100, 0);

    for (int i = 1; i <= n; ++i)
        cin >> p[i];

    for (int i = 1; i <= n; ++i)
        ans[p[p[i]]] = i;

    for (int i = 1; i <= n; ++i)
        cout << ans[i] << endl;

    return 0;
}