vote = int(input())
score = list(map(str, input()))

A = score.count("A")
B = score.count("B")

if A > B:
    print("A")
elif A < B:
    print("B")
else:
    print("Tie")