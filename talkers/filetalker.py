### This file handles the file stuff

def openFile(filename):
    
    try:
        file = open(filename, 'r')
    except FileNotFoundError:
        print(f"Error: the file '{filename}' does not exist.")
        exit(-1)

    for line in file:
        print(line.strip())


if __name__ == "__main__":
    openFile("Goblins.ydk")

    