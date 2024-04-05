import argparse

# parser = argparse.ArgumentParser(description = 'Process some integers.')
# parser.add_argument('integers', metavar = 'N', type = int, nargs = '?', help = 'an integer for the accumulator')
# parser.add_argument('--sum', dest = 'accumulate', const = 'sum', default = max, 
#                     help = 'sum the integers (default is finding the max value)')
# args = parser.parse_args()
# print(args.accumulate(args.integers))

# parser = argparse.ArgumentParser(
#     prog = 'Process some integers',
#     description="will process and return result of two integers",
#     epilog = 'blah')

# parser.add_argument('integers', metavar = 'N', type = int, nargs = '+',
#                     help = 'an integer for the accumulator')
# parser.add_argument('--sum', dest='accumulate', action='store_const',
#                     const=sum, default=max,
#                     help='sum the integers (default: find the max)')

# args = parser.parse_args()
# print(args.filename, args.count, args.verbose)

# parser = argparse.ArgumentParser()
# parser = argparse.ArgumentParser(prog='myprogram')
# parser.add_argument('--foo', help='foo help')
# args = parser.parse_args()

# parser = argparse.ArgumentParser()
# parser.add_argument('filename')
# args = parser.parse_args()
# print(args)

# Spec out for command line
    # - will I be able to write everything on the commandline as args and use throughout program???
    # generating key file
        # - maybe I don't need the key file here --> just need the count of chars to be generated???
        # C: [binary file] [-a] [key] [key count] [file name]
        # P: [python3] []
    # encodeing
        # here will need plaintext, will need key file
     #decoding
        # will need encoded file and key file


def main():
    parser = argparse.ArgumentParser()
    #options for command line
    # add key generation information
    parser.add_argument('-k', '--key', dest = 'key file', action = 'store_const', metavar = 'N', type = int, const = 256, help = 'Count of chars to generate for key file to hold')
    parser.add_argument('-e', '--encode', dest = 'encode file', help = 'Name of file to hold encoded text (plaintext text converted using key)')
    parser.add_argument('-d', '--decode', dest = 'decode file', help='Name of file holding decoded messaage (encoded text converted to plaintext)')
    

    args = parser.parse_args()
    print(args)
    # print(args.key)

if __name__ == "__main__":
    main()