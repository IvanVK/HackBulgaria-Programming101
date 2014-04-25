import sys
from random import randint

def generate_numbers(filename,n):
    file = open(filename,"w")
    while n > 0:
        if n != 1:
            file.write(str(randint(1, 1000)) + " ")
        else:
            _ile.write(str(randint(1, 1000)))
        n -= 1
    file.close()

def main():
    generate_numbers(sys.argv[1],sys.argv[2])

if __name__ == '__main__':
    main()