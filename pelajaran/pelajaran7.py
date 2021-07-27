def main():
    print()

    def recursive(nombor):
        # print()
        if (nombor < 10):
            print(nombor)
            nombor = nombor + 1
            recursive(nombor)

    nombor = 0
    recursive(nombor)


if __name__ == '__main__':
    main()