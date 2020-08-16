// find longest no of elements in a correct parenthesis array
//not working currently
#include <iostream>
#include <stack>
#include <string.h>
using namespace std;
int maxCorrect(string s)
{
    int m = 0;
    stack<char> S;

    // S.push('N');
    for (char ch : s)
    {
        if (ch == '(')
        {
            S.push(ch);
            // cout << S.top() << " ";
        }
        else if (ch == ')' && S.top() == '(')
        {
            S.pop();
            // cout << S.top() << " ";
            m++;
        }
    }
    return m;
}
int main()
{
    string s;
    cin >> s;
    int m = 0;
    for (int i = 0; i < s.size(); i++)
    {
        string sub = s.substr(i, s.size() - i);
        // if (int a = maxCorrect(sub) > m)
        //     m = a;
        cout << maxCorrect(sub) << " ";
    }
    // cout << m;
}
