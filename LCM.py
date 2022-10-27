a, b = map(int, input().split()) # 17 997
i = max(a, b) # 7654321
while True:
    if i % a == 0 and i % b == 0:
        print(i)
        break
    i += 1
