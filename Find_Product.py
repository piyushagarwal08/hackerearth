N = int(input())
array = list(map(int,input().split()))
answer = 1
for i in array:
    answer = (answer*i) % (10**9 + 7)
print(answer)
