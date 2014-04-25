import sys

def cat2(files):
        content =[]
        for filename in files:
            file = open(filename,"r")
            content.append(file.read())
            file.close()
        return "\n".join(content)

def main():
    print(cat2(sys.argv[1:]))

if __name__ == '__main__':
    main()