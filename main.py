import sys


VERSION = "0.0.1"
KEYWORD = ["doc_title", "sub_title", "text", "bar", "author"]
SPECIAL_KEYWORD = ["bar"]  # special keyword are keyword that doesn't need attribut


def parse_document(file):
    raw_file = open(file)
    f = raw_file.read()
    parsed_document = f.split("\n")
    parsed_document_temp = []
    for iteration, line in enumerate(parsed_document):
        iteration = iteration + 1  # That will not break anything
        if not (line.startswith("[") and line.endswith("]")):
            print("Error at line: %s" % iteration)
            print("Line not starting and ending with [ or ]")
            exit(-1)
        line = line[1:-1]  # Remove the first and the last character of a string
        line = line.split(":")
        if not line[0] in KEYWORD:
            print("Error at line: %s" % iteration)
            print("Keyword not recognized: %s" % line[0])
            exit(-1)
        if line[0] in SPECIAL_KEYWORD:
            line_parsed = {line[0]: line[0]}
        else:
            line_parsed = {line[0]: line[1]}
        parsed_document_temp.append(line_parsed)
    raw_file.close()
    parsed_document = parsed_document_temp
    parsed_document_dict = {}
    for dictionary in parsed_document:  # bad code for merging all the dictionary
        parsed_document_dict.update(dictionary)
    return parsed_document_dict


if not len(sys.argv) == 2:
    print("Have you tried putting a/only one file as a argument?")

print("QuickDoc V." + str(VERSION))
print("Starting parsing")
document = parse_document(sys.argv[1])
print("Finished parsing; Starting compiling")
print(document)
