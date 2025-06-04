
#include<bits/stdc++.h>
#include<iostream>
#define ll long long

using namespace std;

int main(){
	int n; cin >> n;
	vector<int> numbers(n);

	for(int i = 0; i < n; i++) cin >> numbers[i];

	int x, a, b;

	cin >> x >> a >> b;

	numbers.erase(numbers.begin()+x-1);
	numbers.erase(numbers.begin()+a-1,numbers.begin()+b-1);

	cout << numbers.size() << endl;

	for(int i = 0; i < numbers.size(); ++i) cout << numbers[i] << " ";

	cout << endl;

	return 0;
}

