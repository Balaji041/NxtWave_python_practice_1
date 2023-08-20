M=int(input())
N=int(input())
string="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
spaces=2*N-3
index=0
for i in range(M):
    eachrow_=""
    for j in range(N):
        if i==0 or i==M-1:
            eachrow_+=string[index]+" "
        elif j==0 :
            eachrow_+=string[index]+ " " * spaces +string[j+index+(N-1)]
        index+=1
    print(eachrow_)
"""
input:
4
6
output:
A B C D E F 
G         L
M         R
S T U V W X
"""
