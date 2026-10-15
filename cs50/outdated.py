import re
list1=[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"]
while True:
    x=input('date:')
    s=re.split(r'[/\-, ]',x)
    if len(s)==3:
        m=s[0]
        d=s[1]
        y=s[2]
        if not (d.isdigit() and y.isdigit()):
           print('error')
        elif int(d)<0 or int(d)>31:
            print('重新输入日期')
        elif m.isdigit():
            print(f"{y}-{m}-{d}")
            break
        else:
            if m in list1:
                    mon=list1.index(m)+1
                    print(f"{y}-{mon}-{d}")
            else:
                print('error')
            break
    else:
        print('error,again')


           
      



 
