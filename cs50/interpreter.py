import re
s = input('请输入算式：')
parts=re.split(r'(\+|\-|\*|/)', s)
x=int(parts[0])
z=int(parts[2]) 
y=parts[1] 
if y=='+':
    print(x+z)  
elif y=='-':
    print(x-z)
elif y=='*':
    print(x*z)
else:
    print(x/z)
