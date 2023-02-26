def choice1(inputforencryption, layers):
    for element in inputforencryption:
        translate = wordlist.index(element)
        final = encryption[translate]
        for _ in range(layers-1):
            translate = wordlist.index(final)
            final = encryption[translate]
        print(final, end='')

    print()
    print()
    menu()


def choice2(inputforencryption, layers):
    for element in inputforencryption:
        translate = encryption.index(element)
        final = wordlist[translate]
        for _ in range(layers-1):
            translate = encryption.index(final)
            final = wordlist[translate]
        print(final, end='')

    print()
    print()
    menu()


wordlist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
            'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ' ',
            '`', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+', '_', '=', '?', '.', ':', ',', '<',
            '|']
encryption = ['z', 'x', 'b', 'c', 'u', 'a', 'w', 'y', 'v', 'd', 't', 'e', 's', 'm', 'h', 'r', 'f', 'l', 'g', 'q', 'k',
              'n', 'i', 'o', 'j', 'p', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H',
              'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', '7', '5', '3', '1', '2', '6', '8', '9', '0', '4', '.',
              '=', '_', '+', '-', ')', '(', '*', '&', '^', '%', '$', '#', '@', '!', '~', '`', '|', ':', ' ', '<', ',',
              '?']


def menu():
    print("are you here to scramble or to unscramble?")
    print("1. for scramble 2. for descramble")
    choice = input()

    print("enter what you want to process: ")
    inputforencryption = input()

    print("how many layers of scrambling / unscrambling? (how much times "
          "do you want it to scramble / unscramble over itself")
    print()
    layers = 0
    layers = int(input())

    if choice == '1':
        print()
        choice1(inputforencryption, layers)
    elif choice == '2':
        print()
        choice2(inputforencryption, layers)

    else:
        print('error')
        exit()


menu()
