
#Caesar's cypher
#Introduce ROT-X (de)coder
#>>> encode('Hello python!')
#'Hryyb clguba!'
#>>> decode('Hryyb clguba!')
#'Hello python!'
#Bonus: dynamic rotation


def encode(text, key):      
    alph = ('abcdefghijklmnopqrstuvwxyz')
    # key = int(raw_input('Enter rotation key (1 - 26): '))

    if key == 0 or key > 26:
        return 'Invalid key!'
        # key = int(raw_input('Enter rotation key (1 - 26): '))
    else:
        shift_alph = alph[key:] + alph[:key]

        ct = [] 
        for i in text:
            if (i in alph) == False: #check for special characters, capital leters will remain the same
                ct += [i]
                continue
            else:
                l_pos = int(alph.index(i))
                cl = shift_alph[l_pos]
                ct += cl
        return (''.join(ct)) 
          
    

def decode(ct, key):     
    alph = ('abcdefghijklmnopqrstuvwxyz')
    # key = int(raw_input('Enter rotation key (1 - 26): '))
    if key > 26 or key == 0:
        return 'Invalid key!'
        # key = int(raw_input('Enter rotation key (1 - 26): '))

    else:
        shift_alph = alph[key:] + alph[:key]

        text = []
        for i in ct:
            if (i in shift_alph) == False:
                text += [i]
            else:
                cl_pos = int(shift_alph.index(i))
                letter = alph[cl_pos]
                text += letter
        return (''.join(text)) 


