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
    print("it made it to encode()")
    return 'dune'

def main():
    #generate parser and fill with appropriate command line arguments
    parser = argparse.ArgumentParser(prog='otp',
                                    description='otp (one time pad) is a program which recieves a message, either plaintext or encrypted, and performs encryption or decryption using a random key',
                                    epilog='thanks for using my %(prog)s program :)')    
    #otp arguments
    parser.add_argument('-ver', '--version', default= 1, type=bool)
    #grouping command keywords together
    group = parser.add_mutually_exclusive_group(required=True)
    #arguments for key generation
    group.add_argument('-keygen', action='store_true', help="command for generation of key for encoding and decodying text")
    group.add_argument('-encode', action='store_true', help="command to initiate encoding of plaintext to ciphertext")
    group.add_argument('-decode', action='store_true', help='name of file holding decoded messaage (encoded text converted to plaintext)') #convert this to take decode.txt file

    parser.add_argument('-k', '--key-file', dest = 'key_text', default='key.txt', help = 'file to be generated opened') #convert this to key file 
    parser.add_argument('-l', '--length', help = 'count of chars to generate for key file to hold') #convert this to key file 
    parser.add_argument('-s', '--seed', dest='seed_value', help='provide a value to use to seed the random generator: for debuggging purposes')
    #arguments for encoding of plaintext/original message
    # parser.add_argument('encode', help="command to initiate encoding of plaintext to ciphertext")
    parser.add_argument('-i', '--input_file', dest = 'input_file',  help = 'name of file to be used containing message for encoding') #convert this to take encode.txt file
    parser.add_argument('-t', '--text', dest='cl_text', help = 'specify input text directly from command line for encoding') 
    parser.add_argument('-T', '--file_text', dest='file_text', help = 'the message to be encoded') 
    parser.add_argument('-o', '--output_file', dest='output_file', help = 'filename to be used for encoded message')
    parser.add_argument('-v', '--verbose', help='provide greater depth of help test')
    args = parser.parse_args()
    print(args, file=sys.stderr)

    #beginning of UI/CL interface
    #generate key file consisting of random chars for encoding and decoding plaintext and ciphertext
    if args.key_text is not None: # and (args.encode is None or args.decode is None):
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
        if args.cl_text is not None and args.file_text is not None:
            print("usage error: only one importation of plaintext allowed", file=sys.stderr)
        if args.cl_text is not None or args.file_text is not None:
            try:
                if args.cl_text is not None and (args.file_text is None and args.input_file is not None):
                    #if -p flag used will pull text directly from command line from user
                    #will write text to new file created
                    with open(args.input_file, "w+") as f_plaintext:
                        f_plaintext.write(args.plaintext)
                        pt_data = f_plaintext.read(args.plaintext)
                        # sys.stdout.write(args.plaintext)
                #will open text file and read into stdout handle for redirection on command line
                elif args.file_text is not None and args.cl_text is None:
                    with open(args.input_file, "r") as f_plaintext:
                        pt_data = f_plaintext.read(args.input_file)
            except FileNotFoundError as err:
                print(err)
        plaintext_len = len(pt_data)
        #generate encoding of original msg using key file and original plaintext file
        #this will create the ciphertext file
        if args.encode is not None and (args.key_text is None and args.decode is None):
            # print("demitri first", file=sys.stderr) #printing to stdout but with pipe goes to decoder aka stdin of decoder
            #generate ciphertext by calling fx passing key, plaintext
            ciphertext = encode(alpha, key_data, pt_data, plaintext_len)
            print(ciphertext)
            try:
                with open(args.output_file, 'w+') as cipher:
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

