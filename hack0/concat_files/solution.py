import sys

def main(filenames):
    contents = []
    filenames = sys.argv[1:]
    for i in filenames:
        file = open(i, "r")
        contents.append(file.read())
        file.close()
    file = open("MEGATRON", "w")
    file.write("\n".join(contents))
    file.close()


if __name__ == "__main__":
    main()