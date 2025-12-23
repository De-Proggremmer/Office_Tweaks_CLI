from sys import argv

from interactive_menu import menu
from cli_parser import parce

main = None
print(argv)
if (len(argv) == 2 and argv[1] == "-i") or len(argv) == 1: main = menu
else: main = parce


if __name__ == "__main__":
    main()