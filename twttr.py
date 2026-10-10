input=(input('input:'))
for i in input.lower():
    if i in['a','e','i','o','u']:
        input=input.replace(i,'')

print(input)
