M=int(input())
N=int(input())
if M>N:
    small=N
else:
    small=M
greatest=0
for i in range(1,small+1):
    if(M%i==0 and N%i==0):
        greatest=i
print(greatest)
"""
input:
4
6
output:
2

"""
