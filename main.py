import sys

VERSION = "0.0.1"

print(sys.argv)
if not len(sys.argv) == 2:
    print("Have you tried putting a/only one file as a argument?")
