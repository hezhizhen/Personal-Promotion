#include <iostream>
using namespace std;

int main()
{
    int a[100];
    int index=0;
    cin >> a[index];
    while(a[index]!=42)
    {
        index++;
        cin >> a[index];
    }
    for(int i=0;i<index;i++)
    {
        cout << a[i] << endl;
    }
    return 0;
}
