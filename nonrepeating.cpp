#include <iostream>
#include <set>
#include <algorithm>
using namespace std;

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int n;
        cin >> n;
        set<int> A;
        int temp;
        for (int i = 0; i < 2 * n + 2; i++)
        {
            cin >> temp;
            if (A.find(temp) != A.end())
                A.erase(temp);
            else
            {
                A.insert(temp);
            }
        }
        // sort(A.begin(), A.end());
        for (auto i = A.begin(); i != A.end(); i++)
            cout << *i << " ";
        cout << endl;
    }
}