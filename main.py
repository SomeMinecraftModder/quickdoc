import sys


def parse_document(file):
    f = open(file).read()
    parsed_document = f.split("\n")
    for line in parsed_document:
        if not line.startswith("[") and line.endswith("]"):
            print("Error at line:%s")
            print("Line not starting and ending with [ or ]")
            exit(-1)
    return parsed_document


VERSION = "0.0.1"

if not len(sys.argv) == 2:
    print("Have you tried putting a/only one file as a argument?")

print("QuickDoc V." + str(VERSION))
print("Starting parsing")
document = parse_document(sys.argv[1])
