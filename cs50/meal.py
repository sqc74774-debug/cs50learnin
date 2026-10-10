def main():
    time = input('请输入用餐时间：')
    time = convert(time)
    if 7<=float(time)<=8:
        print("早餐时间")
    elif 12<=float(time)<=13:
        print("午餐时间")
    elif 18<=float(time)<=19:
        print("晚餐时间")
    else:
        print("非用餐时间")

def convert(time):
    hours, minutes = time.split(':')
    return float(hours) + float(minutes) / 60

if __name__ == '__main__':
    main()