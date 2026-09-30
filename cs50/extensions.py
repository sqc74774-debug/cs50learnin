file=input('the name:')
part=file.split('.')
if part[-1] in ['gif','jpg','jpeg','png','pdf','txt','zip']:
    print('.'+part[-1])
else:
    print('applcation')