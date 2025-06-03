#include<bits/stdc++.h>
#include<iostream>
#include<iomanip>

#define ll long long

using namespace std;

int main(){
	int t; cin >> t;
	cout << setiosflags(ios::uppercase);
	cout << setw(0xf) << internal;

	while(t--){
		double A; cin >> A;
		double B; cin >> B;
		double C; cin >> C;

		cout << left << hex << showbase << nouppercase;
		cout << (ll) A << endl;

		cout.precision(2);
		cout << showpos << fixed << setfill('_') << setw(15) << right;
		cout << B << endl;

		cout.precision(9);
		cout << noshowpos << uppercase << scientific;
		cout << C << endl;


	}
	return 0;
}
