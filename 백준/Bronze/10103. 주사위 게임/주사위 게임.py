chang = sang = 100

n = int(input())
for i in range(n) : 
    c_score, s_score = map(int,input().split()) 
    if c_score == s_score : 
        pass
    elif c_score > s_score : 
        sang -= c_score
    else : 
        chang -= s_score

print(chang)
print(sang)