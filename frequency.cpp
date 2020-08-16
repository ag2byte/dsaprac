//given an array find the max occuring element
#include <iostream>
using namespace std;
int main()
{
    int n;
    cin >> n;
    int count[100] = {0};
    // int ar[n];
    int num;
    for (int i = 0; i < n; i++)
    {
        cin >> num;
        count[num] += 1;
    }
    int max = -1;

    for (int i = 0; i < sizeof(count) / sizeof(count[0]); i++)
    {
        if (count[i] > max)
            max = i;
    }

    cout << "MAX:" << max;
}