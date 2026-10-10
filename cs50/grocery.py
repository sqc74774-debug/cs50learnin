dict={}
count=0
try:
    while True:
        item=input("Item: ")
        if item=='':
            continue
        else:
            dict[count]=item
            count+=1
except EOFError:
    pass

for i, v in enumerate(sorted(dict.values(), key=str.upper), start=1):
    print(i, v.upper())