n = int(input())

sum = 0
combination = 0

for x1 in range(0, n+1):
    for x2 in range(0, n+1):
        for x3 in range(0, n+1):
            sum = x1 + x2 + x3
            if sum == n:
                combination += 1
print(combination)