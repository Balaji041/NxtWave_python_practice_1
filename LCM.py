M=int(input())
N=int(input())
if M>N:
    great=M
else:
    great=N
found_lcm=False
for i in range(great,M*N+1):
    if not found_lcm:
        if (i%M==0)and (i%N==0):
            found_lcm=True
            lcm=i
            print(lcm)
"""
input:2
3
output:6
"""
