import argparse
import sys
import random
import time

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "

def decode(alpha, key, key_data, plaintext_count):
    print("did decode", file=sys.stderr)
    return 'a'

def encode(alpha, key, key_data, plaintext_count):
    print("did encode", file=sys.stderr)
    return 'a'

def main():
    #generate and fill parser with appropriate arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-k', '--key', dest = 'key_count', help = 'count of chars to generate for key file to hold')
    parser.add_argument('-e', '--encode', dest = 'encode_file', help = 'name of file to hold encoded text (plaintext text converted using key)')
    parser.add_argument('-d', '--decode', dest = 'decode_file', help='name of file holding decoded messaage (encoded text converted to plaintext)')
    parser.add_argument('-p', '--plaintext', help = 'the message to be encoded') 
    parser.add_argument('-v', '--verbose', help='provide greater depth of help test')
    args = parser.parse_args()

    #beginning of UI/CLI interface
    #generate key file consisting of random chars for encoding and decoding plaintext and ciphertext
    #setting up plaintext to be written to file for use in cat fx 
    if args.key_count is not None:
        key_count = int(args.key_count)
        #open file key.txt for writing
        try:
            with open("key.txt", "w+") as f_key:
                for i in range(key_count):
                    #generate random number 
                    rand_num = random.randrange(27)
                    #use random number as index and extract char from alpha variable to write to key file 
                    #this will create the key to encode the original message
                    rand_char = alpha[rand_num]
                    f_key.write(rand_char)
                # key_data = f_key.read()
                # print(f"Key date is : {key_data}")
                f_key.write('\n')
        except FileNotFoundError as err:
            print(err)
        #generate plaintext file to hold original message for encryption
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
        #obtain key data to use to encode plaintext msg
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
        if args.decode_file is not None:
            time.sleep(1)
            ciphertext = sys.stdin.read()
            #generate new_plaintext by passing key and ciphertext to appropriate fx
            decoded_plaintext = decode(alpha, key_data, ciphertext, plaintext_len)
            try:
                with open("decoded_plaintext.txt", 'w+') as new_plaintext:
                    new_plaintext.write(decoded_plaintext)
            except FileNotFoundError as err:
                print(err)
           
    print(args, file=sys.stderr)
    
if __name__ == "__main__":
    main()

