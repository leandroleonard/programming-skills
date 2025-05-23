#include<bits/stdc++.h>
#define ll long long

using namespace std;

int main()
{
	int t; cin >> t;
	while(t--){
		int i, n; cin >> n;
		vector<ll> numbers(n);

		for(i = 0; i< n; i++) cin >> numbers[i];
		int ans[0];
		for(i = 1; i < n; i++){
			ans = __gcd(ans, numbers[i]);
		}

		if(ans == 1) cout << "YES" << endl;
		else cout << "NO" << endl;
	}
	return 0;
}