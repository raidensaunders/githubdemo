# Raiden Saunders
def main():
    while True:
        print('Menu')
        print('-' *13)
        print('1. Encode')
        print('2. Decode')
        print('3. Quit')

        choice = int(input('PLease enter an option: '))

        if choice == 1:
            password = input('Please enter your password to encode: ')
            stored = encoder(password)
            print('Your password has been encoded and stored!')
        if choice == 2:
            pass
        else:
            break

def encoder(password):
    x = None
    encode = ''
    for i in password:
        x = int(i) + 3
        encode += str(x)
    return encode

if __name__ == '__main__':
    main()

