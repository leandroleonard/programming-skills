#include<bts/stdc++.h>
#include<iostream>

using namespace std;

void printKMax(int arr[], int n, int k){
	deque<int> Qi(k);

	for(int i = 0;i<k;++i){
		while(!Qi.empty() && arr[i] >= arr[Qi.back()]) Qi.pop_back();
		Qi.push_back(i);
	}

	for(;i<n;++i){
		cout << arr[Qi.front()] << " ";
		while((!Qi.empty()) && Qi.front() <= i - k) Qi.pop_front();

		while
	}
}

int main(){
	int t; cin >> t;

	while(t--){
		int n, k; cin >> n >> k;
		int i;
		int arr[n];
		for(i=0;i<n;i++)cin >> arr[i];
		printKMax(arr, n, k);
	}
	return 0;
}