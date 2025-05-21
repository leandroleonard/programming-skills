#include <bits/stdc++.h>

using namespace std;

int main(){
    int count = 0, number;

    for(int i = 0; i < 5; i++){
        cin >> number;
        if(number>=40) count++; 
    }

    if(count>=3) cout << "CAZZ" << endl;
    else cout << "YEARLAG" << endl;

    return 0;
}