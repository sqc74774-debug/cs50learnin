def main():
    plate=input('plate:')
    if is_valid(plate):
        print('Valid')
    else:
        print('Invalid')

def is_valid(s):
    if len(s)<2 or len(s)>6:
        return False
    if not s[0].isalpha() or not s[1].isalpha():
        return False
    if not s[2:].isdigit():
        return False
    if s[2]=='0':
        return False
    return True 

main()