#include<bits/stdc++.h>
#include<iostream>
#define ll long long

using namespace std;

int main()
{
	int q; cin >> q;
	set<int> s;

	for(int i = 0; i< q;i++){
		int op, x; cin >> op >> x;

		switch(op){
			case 1:
				s.insert(x);	
			break;
			case 2:
				s.erase(x);
			break;
			case 3:
				auto it = s.find(x);
				cout << (s.find(x) != s.end() ? "Yes" : "No") << endl;
			break;
		}
	}

	return 0;
}
