def main():

    if (10 < 3 & 10 > 3):
        print('Betul IF')
    elif (11 < 3 | 11 < 4):
        print('Betul ELIF')
    elif (20 > 3):
        print('Betul ELIF 2')
    else:
        print('Salah')

    # True -> True
    # False -> False

    # True & True -> True
    # True & False -> False
    # False & True -> False
    # False & False -> False

    # True | True -> True
    # True | False -> True
    # False | True -> True
    # False | False -> False

    print('main END')


if __name__ == '__main__':
    main()
