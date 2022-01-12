import sys


VERSION = "0.0.1"
KEYWORD = ["doc_title", "sub_title", "text", "bar", "author"]


def parse_document(file):
    f = open(file).read()
    parsed_document = f.split("\n")
    for iteration, line in enumerate(parsed_document):
        iteration = iteration + 1  # That will not break anything
        if not (line.startswith("[") and line.endswith("]")):
            print("Error at line:%s" % iteration)
            print("Line not starting and ending with [ or ]")
            exit(-1)
        line = line[1:-1]  # Remove the first and the last character of a string
        line = line.split(":")
        if not line[0] in KEYWORD:
            print("Error at line:%s" % iteration)
            print("Keyword not recognized: %s" % line[0])
    return parsed_document


if not len(sys.argv) == 2:
    print("Have you tried putting a/only one file as a argument?")

print("QuickDoc V." + str(VERSION))
print("Starting parsing")
document = parse_document(sys.argv[1])
