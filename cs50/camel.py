name=input('name:')
for i in name:
    if i.isupper():
        name = name.replace(i, '-' + i.lower())
print(name)