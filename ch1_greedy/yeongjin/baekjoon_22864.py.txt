# 한 시간 단위, 하루 24시간
# 일: 피로도 +A, 일 +B
# 쉼: 피로도 -C, 일 +0
# 피로도 M 넘으면 번아웃

work_tired, work_do, rest, burnout = map(int, input().split())  # 한 줄로 네 개의 값을 받아옴
tired =0
hour=0
work_done=0

while hour < 24: # <= 이면 24시간일 때 한 번 더 돌아가서 25까지 계산하게 된다.
    if tired+work_tired <= burnout:
        tired+=work_tired
        work_done+=work_do
    else :
        tired -= rest
    if tired <0:
        tired =0
    hour +=1
    
print(work_done)