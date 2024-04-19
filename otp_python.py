import argparse
import sys
import random
import time

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "

#receive ciphertext to be decoded using key 
def decode(alpha, key, key_data, plaintext_count):
    print("did decode", file=sys.stderr)
    return 'today is Friday'

#receive plaintext and key data to generate encoded msg aka ciphertext
def encode(alpha, key, key_data, plaintext_count):
    print("did encode", file=sys.stderr)
    return 'a'

def main():
    #generate parser and fill with appropriate command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-k', '--key', dest = 'key_text', help = 'file to be generated opened') #convert this to key file 
    parser.add_argument('-N', '--length', dest = 'key_length', help = 'count of chars to generate for key file to hold') #convert this to key file 
    parser.add_argument('-e', '--encode', dest = 'encode_file', help = 'name of file to hold encoded text (plaintext text converted using key)') #convert this to take encode.txt file
    parser.add_argument('-d', '--decode', dest = 'decode_file', help='name of file holding decoded messaage (encoded text converted to plaintext)') #convert this to take decode.txt file
    parser.add_argument('-p', '--plaintext', help = 'the message to be encoded') 
    parser.add_argument('-v', '--verbose', help='provide greater depth of help test')
    args = parser.parse_args()

    ###add another arg that will allow the for using a file as plaintext and NOT BOTH

    #beginning of UI/CLI interface
    #generate key file consisting of random chars for encoding and decoding plaintext and ciphertext
    if args.key_text is not None:
        key_count = int(args.key_length)
        try:
            #generate random number to use as the index to pull a random char from gloabl alpha string variable  
            #this will create the key to encode the original msg
            with open(args.key_text, "w+") as f_key:
                for i in range(key_count):
                    #generate random number 
                    rand_num = random.randrange(27)
                    rand_char = alpha[rand_num]
                    f_key.write(rand_char)
                # key_data = f_key.read()
                # print(f"Key date is : {key_data}")
                f_key.write('\n')
        except FileNotFoundError as err:
            print(err)
        #generate plaintext file to hold original msg
        #will be used in comparing orginal msg with decoded msg using linux diff cmd
        try:
            with open("plaintext.txt", "w") as f_plaintext:
                f_plaintext.write(args.plaintext)
                sys.stdout.write(args.plaintext)
        except FileNotFoundError as err:
            print(err)
    else:
        try:
            with open("key.txt", "r") as file1:
                key_data = file1.read()
        except FileNotFoundError as err:
            print(err)
        f_plaintext = sys.stdin.read()
        plaintext_len = len(f_plaintext)
        #generate encoding of original msg using key file and original plaintext file
        #this will create the ciphertext file
        if args.encode_file is not None:
            # print("demitri first", file=sys.stderr) #printiin to stdout but with pipe goes to decoder aka stdin of decoder
            #generate ciphertext by calling fx passing key, plaintext
            ciphertext = encode(alpha, key_data, f_plaintext, plaintext_len)
            try:
                with open("ciphertext.txt", 'w+') as cipher:
                    cipher.write(ciphertext)
            except FileNotFoundError as err:
                print(err)
            sys.stdout.write(ciphertext)
        #generate decoded original msg using key file and the ciphertext file
        #this will create the original msg store in the variable new_plaintext
        if args.decode_file is not None:
            # time.sleep(1)
            ciphertext = sys.stdin.read()
            #generate new_plaintext by passing key and ciphertext to appropriate fx
            decoded_plaintext = decode(alpha, key_data, ciphertext, plaintext_len)
            try:
                with open("decoded_plaintext.txt", 'w+') as new_plaintext:
                    new_plaintext.write(decoded_plaintext)
            except FileNotFoundError as err:
                print(err)
           
    # print(args, file=sys.stderr)
    
if __name__ == "__main__":
    main()

# Questions
#     - why no error for when piping to diff
    # - documentation appropriate?