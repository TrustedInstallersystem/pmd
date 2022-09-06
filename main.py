import sys

while True:
    content = input(">>>").split(" ")
    if content[0] == "echo":
        print(content[1])
    elif content[0] == "exit":
        sys.exit()
    else:
        print("{:s}:'{:s}' command doesn't exists".format(content[0], content[0]))