
#Caesar's cypher
#Introduce ROT-X (de)coder
#>>> encode('Hello python!')
#'Hryyb clguba!'
#>>> decode('Hryyb clguba!')
#'Hello python!'
#Bonus: dynamic rotation


def encode(text):      
    alph = ('abcdefghijklmnopqrstuvwxyz')
    key = int(raw_input('Enter rotation key (1 - 26): '))

    if key == 0 or key > 26:
        print('Invalid key!')
        key = int(raw_input('Enter rotation key (1 - 26): '))

    shift_alph = alph[key:] + alph[:key]

    ct = [] 
    for i in text:
        if (i in alph) == False: #check for special characters
            ct += [i]
            continue
        else:
            l_pos = int(alph.index(i))
            cl = shift_alph[l_pos]
            ct += cl
    print(''.join(ct))
    return 
#encode('hello python')         
    

def decode(ct):     
    alph = ('abcdefghijklmnopqrstuvwxyz')
    key = int(raw_input('Enter rotation key (1 - 26): '))
    if key > 26 or key == 0:
        print('Invalid key!')
        key = int(raw_input('Enter rotation key (1 - 26): '))

    shift_alph = alph[key:] + alph[:key]

    text = []
    for i in ct:
        if (i in shift_alph) == False:
            text += [i]
        else:
            cl_pos = int(shift_alph.index(i))
            letter = alph[cl_pos]
            text += letter
    print(''.join(text)) 
    return 
