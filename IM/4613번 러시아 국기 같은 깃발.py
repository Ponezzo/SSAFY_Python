import sys
sys.stdin = open('2. input.txt')
    # N개 중에 2개를 뽑는 경우의 변형
    # (0,i+1), (i+1,j+1), (j+1,N)
    # IM: 전체를 순회/반복 (완전탐색)

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    
    
    mx = 0
    for i in range(0,N-2):
        for j in range(i+1, N-1):
            cnt = 0
            for s in range(0, i+1):
                cnt += arr[s].count('W')
            for s in range(i+1, j+1):
                cnt += arr[s].count('B')
            for s in range(j+1, N):
                cnt += arr[s].count('R')
            mx = max(mx,cnt)
    print(f'#{tc} {N*M-mx}')
