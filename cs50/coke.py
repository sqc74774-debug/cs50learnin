def main():
    due=50
    while due>0:
        coin=int(input('请输入硬币：'))
        if coin in [25,10,5]:
            due-=coin
            if due>0:
                print('还需支付：',due)
        else:
            print('请输入有效的硬币')
    if due < 0:
        print('支付完成，找零：',-due)
    if due == 0:
        print('支付完成')
main()