#include <iostream>
using namespace std;

int main()
{
    char A[11], B[6];
    cin >> A >> B;

    // check
    bool flag = false;
    for(int i=0;i<=5;i++)
    {
        for(int j=0;j<5;j++)
        {
            if(A[i+j]!=B[j])
            {
                break;
            }
            if(j==4)
            {
                flag = true;
            }
        }
    }
    if(flag)
    {
        cout << 1 << endl;
    }
    else
    {
        cout << 0 << endl;
    }
    return 0;
}
