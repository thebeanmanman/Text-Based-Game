from time import sleep 
def text(toprint):
    texttime = 0.03
    toprint = str(toprint)
    for char in toprint:
        print(char,flush=True,end='')
        if char == '.':
            sleep(texttime*20)
        else:
            sleep(texttime)
    print('\n',end='')