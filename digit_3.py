N=int(input())
for i in range(1,2*N):
    if i==1 or i==2*N-1 or i==(N*2)//2:
        print("* "*N)
    elif (N*2)//2:
        print("  "*(N-1)+"* ")
    else:
        print("  "*(N-1)+"* ")
"""
input:5
output:
* * * * * 
        * 
        * 
        * 
* * * * * 
        * 
        * 
        * 
* * * * * 
"""
