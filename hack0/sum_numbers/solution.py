import sys

def sum_numbers(filename):
    filename = sys.argv[1]
    file = open(filename, "r")
    content = file.read()
    result = 0
    result = sum(map(int, content.split(" ")))
    return result
    file.close()

def main():
	filename = sys.argv[1]
	print (sum_numbers(filename))
	

if __name__ == '__main__':
	main()