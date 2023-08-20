N=int(input())
s=1
for i in range(1,N+1):
    print(". "*(N-i)+"0 "*s+". "*(N-i))
    s+=2
"""
input:5
output:
. . . . 0 . . . . 
. . . 0 0 0 . . . 
. . 0 0 0 0 0 . . 
. 0 0 0 0 0 0 0 . 
0 0 0 0 0 0 0 0 0
"""
