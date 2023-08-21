M=int(input())
N=int(input())
if not(M>1):
    M=2
no_prime=True
for i in range(M,N+1):
    is_prime=True
    for j in range(2,i):
        if i%j==0:
            is_prime=False
            break
    if is_prime:
        print(i)
        no_prime=False
        break
if no_prime:
    print("No prime numbers in the given range")
"""
input:25
50
output:29
"""
        
   
       
        
            
        
        
        
