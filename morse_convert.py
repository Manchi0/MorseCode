m_dict= { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}
rm_dict={
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F',
    '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L',
    '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R',
    '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
    '-.--': 'Y', '--..': 'Z', '.----': '1', '..---': '2', '...--': '3',
    '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8',
    '----.': '9', '-----': '0', '--..--': ', ', '.-.-.-': '.', '..--..': '?',
    '-..-.': '/', '-....-': '-', '-.--.': '(', '-.--.-': ')'
}



def morse_encrypt(words):
    print(1)
    lst=[]
    converted=[]
    words=words.upper()
    for i in words:
        lst+=i

    for j in lst:
        if j in m_dict:
            converted+=[m_dict[j]]
        else:
            converted+=[j]
    print(' '.join(converted))

def morse_decrypt(words):
    lst=[]
    converted=[]
    lst1=words.split('  ')

    for i in range(len(lst1)):
        k=lst1[i]
        lst+=k.split(' ')
        lst+=[' ']

    for j in lst:
        if j in rm_dict:
            converted+=[rm_dict[j]]
        else:
            converted+=[j]
    converted.pop(len(converted)-1)
    print(''.join(converted))

while True:
    choice=int(input("\n1 for Text to Morse, 2 For Morse to text: "))
    x=input('Provide text to be converted in as single line: ')
    if choice==1:
        morse_encrypt(x)
    elif choice==2:
        morse_decrypt(x)
    else:
        print('Enter 1 or 2 please')
    

