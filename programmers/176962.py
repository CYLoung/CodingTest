'''
💡 Key
- 옛날에 풀었던 요격 시스템 투포인터 알고리즘이랑 동일 할 것 같음
- 3 <= plans <= 1000
- 진행중이던 과제를 끝냈을 때 잠시 멈춘 과제가 있다면 멈춰둔 과제를 이어서 진행 
- plans : [name, start, playtime]
- name : 과제의 이름 2 ~ 10 / 알파벳 소문자 / name 중복 원소는 없음
- start : 시작 시각 / hh:mm
- playtime :1~100 , 0으로 시작 되지 않음 -> 분임
- 진행 중이던 과제가 끝나는 시각과 새로운 과제를 시작해야하는 시각이 같으면 진행 과제는 끝난 것으로 판단함 

🔑 Strategy
1. plans를 시작시간 기준으로 오름차순 정렬
2. 시간 계산을 편하게 하기 위해 시작시간의 hh:mm을 분단위로 계산해 교체
3. plans를 순회하며 차례로 종료시간과 다음 시작시간을 비교함
- 종료시간이 다음 시작 시간보다 클경우 wait 공간에 추가
- 종료시간이 다음 시작 시간보다 작거나 같을 경우 answer에 추가
    - 여유값을 구하고 , wait에 중단 과제가 있을 경우 여유시간이 1이상일 떄 최근 중단 과제 재개
4. 순회 후 wait에 중단 과제가 있으면 끝에서 부터 차례로 answer에 추가

🔑 Feedback

'''

def solution(plans):
    plans = sorted(map(lambda x: [x[0], int(x[1][:2]) * 60 + int(x[1][3:]), int(x[2])], plans), key=lambda x: -x[1])
    
    lst = []
    while plans:
        x = plans.pop()
        for i, v in enumerate(lst):
            print(v[0], x[1])
            if v[0] > x[1]: # compare end time (curr end & next start) 
                lst[i][0] += x[2] # add curr end + next play time
        lst.append([x[1] + x[2], x[0]]) # [end, name]
    lst.sort()

    return list(map(lambda x: x[1], lst))