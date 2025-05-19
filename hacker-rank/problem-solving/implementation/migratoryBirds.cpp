#include <bits/stdc++.h>

using namespace std;

int main()
{
    map<int, int> mb;
    int birds;
    cin >> birds;
    vector<int> numbers(birds);
    for (int i = 0; i < birds; i++)
    {
        cin >> numbers[i];
        if (mb.find(numbers[i]) == mb.end())
        {
            mb[numbers[i]] = 1;
        }
        else
        {
            mb[numbers[i]] += 1;
        }
    }

    int result = numbers[0], max = mb[numbers[0]];
    for (int i = 1; i < birds; i++)
    {
        if (max < mb[numbers[i]])
        {
            max = mb[numbers[i]];
            result = numbers[i];
        }
        else if (max == mb[numbers[i]] && result > numbers[i])
        {
            result = numbers[i];
        }
    }

    cout << result << endl;

    return 0;
}