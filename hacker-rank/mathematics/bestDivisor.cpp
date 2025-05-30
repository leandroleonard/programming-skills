#include<bits/stdc++.h>
#define ll long long

using namespace std;

ll sum_digits(ll n){
	ll sum = 0;
	
	string number = to_string(n);
	for(int i = 0;i< number.size(); i++){
		sum += number[i] - '0';
	}

	return sum;
}

int main()
{
	ll n; cin >> n;
	ll result = 0;
	for(ll i = 0; i <= n; i++){
		if(sum_digits(i) > sum_digits(result) && n % i == 0) result = i;
	}

	cout << result << endl;
	return 0;
}