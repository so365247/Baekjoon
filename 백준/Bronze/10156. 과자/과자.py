#K = 과자 가격
#N = 과자 개수 
#M = 가진 돈

K, N, M = map(int,input().split())

mom = K * N - M
if mom <= 0:
    print(0)
else:
    print(mom)