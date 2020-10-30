# taken from: https://www.tutorialspoint.com/python3/python_command_line_arguments.htm

import sys, getopt


def getoption(argv):
    author = ''
    subfolder = ''
    genuinefile01 = ''
    genuinefile02 = ''
    forgedfile = ''
    try:
        opts, args = getopt.getopt(argv, "ha:s:o:t:f:",
                                   ["author=", "subfolder=", "ogenuinefile01=", "tgenuinefile02=", "forgedfile="])
    except getopt.GetoptError:
        print('compare.py -a <author> -s <subfolder> -o <genuinefile01> -t genuinefile02  -f <forgedfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('compare.py -a <author> -s <subfolder> -o <genuinefile01> -t genuinefile02 -f <forgedfile>')
            sys.exit()
        elif opt in ("-a", "--author"):
            author = arg
        elif opt in ("-s", "--subfolder"):
            subfolder = arg
        elif opt in ("-o", "--genuinefile01"):
            genuinefile01 = arg
        elif opt in ("-t", "--genuinefile02"):
            genuinefile02 = arg
        elif opt in ("-f", "--forgedfile"):
            forgedfile = arg
    print('Author is "', author)
    print('Subfolder is "', subfolder)
    print('Genuine File 01 is "', genuinefile01)
    print('Genuine File 02 is "', genuinefile02)
    print('Forged File is "', forgedfile)

    # return tuple of values
    return (author, subfolder, genuinefile01, genuinefile02, forgedfile)


def main(argv):
    getoption(argv)


if __name__ == "__main__":
    main(sys.argv[1:])
