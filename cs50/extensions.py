file=input('the name:')
part=file.split('.')
if part[-1] in ['gif','jpg','jpeg','png','pdf','txt','zip']:
    if part[-1]=='gif':
        print('image/gif')
    elif part[-1]=='jpg' or part[-1]=='jpeg':
        print('image/jpeg')
    elif part[-1]=='png':
        print('image/png')
    elif part[-1]=='pdf':
        print('application/pdf')
    elif part[-1]=='txt':
        print('text/plain')
    elif part[-1]=='zip':
        print('application/zip')
else:
    print('application/octet-stream')
