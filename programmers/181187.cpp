/* 
💡 Targets
- 주어진 두개의 원 사이 공간의 정수 x,y 좌표 값의 개수를 리턴 하여라

🔑 Strategy
- 원 외곽에 해당하는 부분으로 인해 발생하는 점의 갯수 (각 4개)
- 두개의 원 사이에 발생할 수 있는 점의 갯수(4x3x(r2-r1)) - 4

🔑 Solution


*/

#include <string>
#include <vector>

using namespace std;

long long solution(int r1, int r2) {
    long long answer = 0;
    if ((r2-r1)==1)
        answer = 8 + 3 *4* (r2-r1);
    else
        answer = 4 + 3 *4* (r2-r1);

    return answer;
}