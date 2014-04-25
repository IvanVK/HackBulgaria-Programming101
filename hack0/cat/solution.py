import sys

def cat(filename):
    file  = open(filename,'r')
    content = file.read()
    file.close()
    return content

def main():
    print (read_file(filename))

if __name__ == '__main__':
    main()