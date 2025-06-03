#include<bits/stdc++.h>
#include<iostream>

using namespace std;

#define ll long long

int main(){
	int n; cin >> n;

	vector<int> v(n);

	for(int i = 0; i < n; ++i) cin >> v[i];

	int q; cin >> q;

	for(int i = 0; i < q; ++i){
		int y; cin >> y;

		auto it = lower_bound(v.begin(), v.end(), y);

		
		if(*it == y) cout << "YES " << distance(v.begin(), it) + 1 << endl;
		else cout << "No " << distance(v.begin(), it) + 1 << endl;	
	}

	return 0;
}
