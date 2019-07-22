Pjy,Qjy=map(int,input().split())
Li=list(map(int,input().split()))[:Pjy]
rd=int(input())
S=(sum(Li)-Li[Qjy])//2
if (S==rd):
    print("Bon Appetit")
else:
    print(abs(S-rd))
