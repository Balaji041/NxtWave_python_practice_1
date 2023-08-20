N=int(input())
k=int(input())
for i in range(N):
    if N%(N-i)==0:
        largest=N-i
        k-=1
    if k==0:
        break
print(largest)
"""
input:
12
2

output:6
"""
