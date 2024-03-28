money = 0

while True:
    n = int(input())
    if n == -1:
        break
    money = n + money
    
print(money)