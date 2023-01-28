T = int(input())
money = {}
for i in range(0, T):
    money[i] = list(map(int, input().split()))

for j in range(0, T):
    print(money[j][0] - money[j][1])

