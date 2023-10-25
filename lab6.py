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
        elif choice == 2:
            original_pass = decode(password)
            print(f'The encoded password is {stored}, and the original password is {original_pass}.')
            pass
        else:
            break

def encoder(password):
    x = None
    encode = ''
    for i in password:
        x = int(i) + 3

        if x >= 10:
            x -= 10

        encode += str(x)
    return encode

def decode(password):
    return password


if __name__ == '__main__':
    main()

