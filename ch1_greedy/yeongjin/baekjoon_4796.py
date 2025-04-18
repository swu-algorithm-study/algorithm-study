case_num=1

while True:
    L, P, V = map(int, input().split())
    
    if L == 0 and P == 0 and V == 0:
        break  # 0 0 0 입력 시 종료

    periods = V // P  # 완전한 주기 개수
    days = periods * L  # 전체 주기에서 캠핑할 수 있는 총 일수
    days += min(L, V % P)  # 남은 날 중 캠핑할 수 있는 날만 추가
    
    print(f"Case {case_num}: {days}")
    case_num += 1  # 케이스 번호 증가