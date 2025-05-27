#include<bits/stdc++.h>
#include<iostream>
#include<string>

using namespace std;

int main(){
	int q; cin >> q;
	map<string, int> m;

	while(q--){
		int op; cin >> op;
		string name; cin >> name;

		switch(op){
			case 1:
				int mark; cin >> mark;

				if (m.find(name) != m.end()) m[name] += mark;
				else m[name] = mark;
			break;
			case 2:
				m.erase(name);
			break;
			case 3:
				if(m.find(name) != m.end()) cout << m[name] << endl;
				else cout << 0 << endl;
			break;
		}
	}
	return 0;
}

