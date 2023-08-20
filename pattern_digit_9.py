N=int(input())
for i in range(1,N*2):
    if i==1 or i==(N*2-1) or i==((N*2)//2):
        print("* "*N)
    elif(i<((N*2)//2)):
        print("* "+"  "*(N-2)+"* ")
    else:
        print("  "*(N-1)+"* ")
"""
input:4
output:
* * * * 
*     * 
*     * 
* * * * 
      * 
      * 
* * * *
"""
