import argparse
import sys
import random
import time

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "

def get_index_value(character, plaintext_len):
    for i in range(plaintext_len):
        if character == alpha[i]:
            return i 

#receive ciphertext to be decoded using key 
def decode(alpha, key, plaintext, plaintext_count):
    print("did decode", file=sys.stderr)
    return 'howdy sunday'

#receive plaintext and key data to generate encoded msg aka ciphertext
def encode(alpha, key, plaintext, plaintext_count):
    #obtain each char from key and plaintext 
    #sum together by and take modulus of length of alpha variable
    #for i in range(len(plaintext)):
        #get value of key[i] 
        #get value of plaintext[i]
        #sum values and take modulus
        #retrieve char from alpha variable based on sum
    ##decide whether to write to file here or return each char##

    return 'a'

def main():
    #generate parser and fill with appropriate command line arguments
    parser = argparse.ArgumentParser()    
    #otp arguments
    parser.add_argument('-ver', '--version', default= 1, type=bool)
    #arguments for key generation
    parser.add_argument('keygen', help="command for generation of key for encoding and decodying text")
    parser.add_argument('-k', '--key-file', dest = 'key_text', default='key.txt', help = 'file to be generated opened') #convert this to key file 
    parser.add_argument('-l', '--length', help = 'count of chars to generate for key file to hold') #convert this to key file 
    parser.add_argument('-s', '--seed', dest='seed_value', help='provide a value to use to seed the random generator: for debuggging purposes')
    #arguments for encoding of plaintext
    parser.add_argument('-e', '--encode', help='name of file to write ciphertext to')
    #plaintext can be taken directly from command line, from a file or passed along via redirection 
    parser.add_argument('-i', '--input_file', dest = 'input_file',  help = 'name of file to be used storing message for encoding') #convert this to take encode.txt file
    parser.add_argument('-t', '--text', dest='text', help='specify input text directly for encoding')
    parser.add_argument('-d', '--decode', help='name of file holding decoded messaage (encoded text converted to plaintext)') #convert this to take decode.txt file
    parser.add_argument('-p', '--plaintext', help = 'the message to be encoded') 
    parser.add_argument('-v', '--verbose', help='provide greater depth of help test')
    parser.add_argument('-P', '--plaintext_file', help='file with plaintext to be used for encoding')
    args = parser.parse_args()
    print(args, file=sys.stderr)

    #beginning of UI/CL interface
    #generate key file consisting of random chars for encoding and decoding plaintext and ciphertext
    if args.key_text is not None and (args.encode is None or args.decode is None):
        try:
            if args.seed_value is not None:
                random.seed(args.seed_value)
            #generate random number.This will be used as the index value to 'grab' a random char from the global alpha string variable  
            #will create the key for encoding the original msg
            with open(args.key_text, "w+") as f_key:
                for i in range(int(args.length)):
                    #generate random number 
                    rand_num = random.randrange(27)
                    rand_char = alpha[rand_num]
                    f_key.write(rand_char)
                f_key.write('\n')
        except FileNotFoundError as err:
            print(err)
    else:
        try:
            with open(args.key_text, "r") as key_file:
                key_data = key_file.read()
        except FileNotFoundError as err:
            print(err)
        #generate plaintext file to hold original msg
        #will be used in comparing orginal msg with decoded msg using linux diff cmd
        if args.plaintext is not None and args.plaintext_file is not None:
            print("usage error: only one importation of plaintext allowed", file=sys.stderr)
        if args.plaintext is not None or args.plaintext_file is not None:
            try:
                if args.plaintext is not None and args.plaintext_file is None:
                    #if -p flag used will pull text directly from command line from user
                    #will write text to new file created
                    with open(args.input_file, "w+") as f_plaintext:
                        f_plaintext.write(args.plaintext)
                        # sys.stdout.write(args.plaintext)
                #will open text file and read into stdout handle for redirection on command line
                # elif args.plaintext_file is not None and args.plaintext is None:
                #     with open(args.plaintext_file, "r") as f_plaintext:
                #         pt_data = f_plaintext.read(args.plaintext)
                #         # sys.stdout.write(pt_data)
            except FileNotFoundError as err:
                print(err)
        try:
            with open()
        #plaintext received from command line redirection via stdout
        # f_plaintext = read()
        plaintext_len = len(f_plaintext)
        #generate encoding of original msg using key file and original plaintext file
        #this will create the ciphertext file
        if args.encode is not None:
            # print("demitri first", file=sys.stderr) #printiin to stdout but with pipe goes to decoder aka stdin of decoder
            #generate ciphertext by calling fx passing key, plaintext
            ciphertext = encode(alpha, key_data, pt_data, plaintext_len)
            try:
                with open(args.encode, 'w+') as cipher:
                    cipher.write(ciphertext)
                    print(f"encode done!")
            except FileNotFoundError as err:
                print(err)
            sys.stdout.write(ciphertext)
        #generate decoded original msg using key file and the ciphertext file
        #this will create the original msg store in the variable new_plaintext
        if args.decode is not None:
            ciphertext = sys.stdin.read()
            #generate new_plaintext by passing key and ciphertext to appropriate fx
            decoded_plaintext = decode(alpha, key_data, ciphertext, plaintext_len)
            try:
                with open(args.decode_file, 'w+') as new_plaintext:
                    new_plaintext.write(decoded_plaintext)
            except FileNotFoundError as err:
                print(err)
            sys.stdout.write(decoded_plaintext)
    
if __name__ == "__main__":
    main()

