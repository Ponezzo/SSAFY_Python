import sys
sys.stdin = open('2. input.txt')

N, M = map(int, input().split()) # N = 세로(y축) , M = 가로(x축)
arr = [input() for _ in range(N)]

y_point, x_point = N-8, M-8
y_points = []
x_points = []

for i in range(y_point):
    y_points.append(i)

for i in range(x_point):
    x_points.append(i)

print(y_points, x_points)

for i in range(4):
    print(arr[i][1])