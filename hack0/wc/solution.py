import sys

def main():
    option = sys.argv[1]
    filename = sys.argv[2]
    file = open(filename,"r")
    content = file.read()
    if option == "chars":
        print(len(content))
    if option == "words":
        print(len(content.split(" ")))
    if option == "lines":
        return len(content.split("\n"))
    file.close()

if __name__ == '__main__':
    main()