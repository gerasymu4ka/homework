
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

    if key == 0 or key > 52:
        print('Invalid key!')
        key = int(raw_input('Enter rotation key (1 - 26): '))

    shift_alph = alph[key:] + alph[:key]

    ct = [] 
    for i in text:
        if i == ' ':
            ct += [i]
        else:
            l_pos = int(alph.index(i))
            cl = shift_alph[l_pos] 
            ct += cl
    print(''.join(ct))
    return 
#encode('hello python')         
    

def decode(ct):     
    alphabet = ('abcdefghijklmnopqrstuvwxyz')
    key = int(raw_input('Enter rotation key (1 - 26): '))
    if key > 26 or key == 0:
        print('Invalid key!')
    key = int(raw_input('Enter rotation key (1 - 26): '))
    before_key = alphabet[:key]
    after_key = alphabet[key:]
    shifted_alphabet = after_key + before_key

    text = []
    for i in ct:
        if i == ' ':
            text += [' ']
        else:
            caesar_letter_position = int(shifted_alphabet.index(i))
            letter = alphabet[caesar_letter_position]
            text += letter
    print(''.join(text)) 
    return 
