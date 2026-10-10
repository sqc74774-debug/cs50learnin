while True:
        try:
            fuel=input('Fraction:')
            x,y=fuel.split('/')
            x=int(x)
            y=int(y)
            if x<0 or y<=0 or x>y:
                raise ValueError
            result=x/y*100
        except (ValueError, ZeroDivisionError):
            print('Invalid input')
            continue
        if result<=1:
                print('E')
        elif result>=99:
                print('F')  
        else:
            print(f'{result:.0f}%')
            break
        