import sys
import os.path

VERSION = "0.0.2"
KEYWORD = ["doc_title", "sub_title", "text", "bar", "author", "list"]
SPECIAL_KEYWORD = ["bar"]  # special keyword are keyword that doesn't need attribut


def compile_html(parsed_input):
    compiled_html = '''<!doctype HTML> <!--Generated using QuickDoc %s-->
<html>
<head>''' % VERSION
    for key in range(len(parsed_input)):
        key += 1
        if parsed_input[key][0] == "doc_title":  # retrieve needed value(s) for <head>
            print("1")
            compiled_html = compiled_html + "<title>%s</title>" % parsed_input[key][1]
    compiled_html = compiled_html + "</head><body>"
    for key in range(len(parsed_input)):
        key += 1
        current_key = parsed_input[key][0]  # retrieve needed value(s) for <head>
        if current_key == "doc_title":
            compiled_html = compiled_html + "<h1>%s</h1>" % parsed_input[key][1]
        if current_key == "sub_title":
            compiled_html = compiled_html + "<h2>%s</h2>" % parsed_input[key][1]
        if current_key == "text":
            compiled_html = compiled_html + "<p>%s</p>" % parsed_input[key][1]
        if current_key == "bar":
            compiled_html = compiled_html + "<hr>"
        if current_key == "author":
            compiled_html = compiled_html + "<address>%s</address>" % parsed_input[key][1]
        if current_key == "list":
            list_html = parsed_input[key][1].split("\n")[:-1]  # magic
            compiled_html = compiled_html + "<ul>"
            for list_element in list_html:
                compiled_html = compiled_html + "<li>%s</li>" % list_element
            compiled_html = compiled_html + "</ul>"
    compiled_html = compiled_html + "</body></html>"
    return compiled_html


def parse_document(file):
    raw_file = open(file)
    f = raw_file.read()
    parsed_document = f.split("\n")
    parsed_document_temp = []
    ignore_list = []
    for iteration, line in enumerate(parsed_document):
        iteration = iteration + 1  # That will not break anything
        if iteration in ignore_list:
            continue
        if not (line.startswith("[")):
            print("Error at line: %s" % iteration)
            print("Line not starting and ending with [ or ]")
            exit(-1)
        else:  # Wait, that maybe is a multi-line keyword?
            is_multi_line_keyword = -1
            for iteration_check_line, checked_line in enumerate(parsed_document[iteration:]):
                if checked_line == "]":  # It is!
                    is_multi_line_keyword = iteration_check_line + iteration
            if is_multi_line_keyword == -1:  # It's not
                print("Error at line: %s" % iteration)
                print("Line not starting and ending with [ or ]")
                exit(-1)
            else:
                line = parsed_document[iteration - 1] + '\n'.join(parsed_document[iteration:is_multi_line_keyword + 1])
                for ignore in range(iteration, is_multi_line_keyword + 2):
                    ignore_list.append(ignore)
        line = line[1:-1]  # Remove the first and the last character of a string
        line = line.split(":", 1)
        if not line[0] in KEYWORD:
            print("Error at line: %s" % iteration)
            print("Keyword not recognized: %s" % line[0])
            exit(-1)
        if len(line) == 2 and line[1].startswith(" "):  # remove the first letter of the keyword value if it's a space
            line[1] = line[1][1:]
        if line[0] in SPECIAL_KEYWORD:
            line_parsed = {iteration: [line[0], line[0]]}
        else:
            line_parsed = {iteration: [line[0], line[1]]}
        parsed_document_temp.append(line_parsed)
    raw_file.close()
    parsed_document = parsed_document_temp
    parsed_document_dict = {}
    for dictionary in parsed_document:  # bad code for merging all the dictionary
        parsed_document_dict.update(dictionary)
    return parsed_document_dict


if __name__ == '__main__':
    if not len(sys.argv) == 2:
        print("Have you tried putting a/only one file as a argument?")
    print("QuickDoc V." + str(VERSION))
    print("Starting parsing")
    document = parse_document(sys.argv[1])
    print("Finished parsing; Starting compiling")
    html = compile_html(document)
    print("Compiling finished!; File saved at %s" % os.path.splitext(sys.argv[1])[0] + ".html")
    f = open(os.path.splitext(sys.argv[1])[0] + ".html", mode="w")  # yes
    f.write(html)
    f.close()
