#include <iostream>
using namespace std;

int main()
{
    int N, count, new_N, A, B;

    cin >> N;

    new_N = N;
    count = 0;
    while ((count == 0) || (new_N != N))
    {
        if (new_N < 10)
        {
            new_N = new_N * 10 + new_N;
        } else
        {
            A = new_N/10;
            B = new_N%10;
            new_N =  B * 10 + (A + B)%10;
        }
        count++;

    }

    cout << count << endl;
    
    return 0;
}
