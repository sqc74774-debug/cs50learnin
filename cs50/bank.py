a=input('Greeting:').lower()
if 'hello' in a:
    print('$0')
elif a[0]=="h" and 'hello' not in a:
    print('$20')
else:
    print('$100')