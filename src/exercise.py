def main():
    #write your code below this line
    names = []
    while True:
        name = input()
        if (name == ""):
            break
        else:
            names.append(name)
    print(names[len(names) - 1])

if __name__ == '__main__':
    main()
