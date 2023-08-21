string=input()
v="a,e,o,i,u,A,E,I,O,U"
s=""
for i in string:
    if i in v:
        continue
    s+=i
print(s)

"""
input:Speak louder
output:
"""
