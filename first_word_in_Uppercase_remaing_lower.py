S=input()
name=""
for i in S:
    if i==" ":
        break
    else:
        name+=i.upper()
      
print(name+S[len(name):])

"""
input:Python is a programming language.
output:PYTHON is a programming language.

"""
