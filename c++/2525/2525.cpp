#include <iostream>
using namespace std;

int main()
{
    int A, B, C; // 입력값
    int H, M; //새로운 시간 설정
    
    cin >> A >> B;
    cin >> C;

    if(B + C < 60)
    {
        H = A;
        M = B + C;
    }
    else
    {
        H = (A + int((B + C) / 60)) % 24;
        M = (B + C) % 60;
    }
    
    cout << H << " " << M;
    return 0;
}