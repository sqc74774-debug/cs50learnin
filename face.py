def convert(word):
    res=word.replace(':)','🙂').replace(':(','🙁')
    return(res)

def main():
    word=input('word:')
    final=convert(word)
    print(final)

main()