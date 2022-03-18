#include <iostream>
using namespace std;

int max_total = 0;      //숫자 3개의 합
int* visited;            // 방문한 숫자 저장
int N, M;               // 카드의 개수, 블랙잭 숫자
int* cards;             // 카드 번호


int blackjack(int k, int total) { //k 현재 카드의 개수, total 세 수의 합
    // 만약 숫자의 합이 M을 넘어가면 return
    if(total > M) {
        return 0;
    }
    if(k == 3) {
        if (abs(max_total-M) > abs(total-M)){
            max_total = total;
            return 0;
        }
    }
    for(int i = 0; i<N; i++) {
        // 현재 카드를 방문한 적이 없으면 해당 카드를 더하고 다음 수를 찾는다.
        if (visited[i] == 0){
            visited[i] = 1;
            blackjack(k+1, total + cards[i]);
            visited[i] = 0;
        }
    }
    return 0;
}


int main(){
    cin >> N >> M;
    
    cards = new int[N];
    visited =  new int[N]{};
    
    for (int i = 0; i < N; i++){
        cin >> cards[i];
    }

    blackjack(0, 0);

    cout << max_total << '\n';
    
    delete visited, cards;
    return 0;
}