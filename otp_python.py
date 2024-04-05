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

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-k', '--key')
    parser.add_argument('-e', '--encode')
    parser.add_argument('-d', '--decode')

    args = parser.parse_args()
    print(args)

if __name__ == "__main__":
    main()