#include <iostream>
using namespace std;

int getMax(unsigned long *ar, int n)
{
    unsigned long m = 0;
    for (int i = 0; i < n - 1; i++)
    {
        for (int j = i + 1; j < n; j++)
        {
            if (ar[i] <= ar[j] && j - i > m)
                m = j - i;
        }
    }
    return m;
}

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        /* code */
        int n;
        cin >> n;
        unsigned long ar[n];

        for (int i = 0; i<n; cin>> ar[i++])
            ;

        cout << getMax(ar, n) << endl;
    }
}