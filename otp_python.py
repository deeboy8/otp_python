import argparse
import sys
import random
import time

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "

def decode(key):
    print("did decode", file=sys.stderr)
    return key 

def encode(key):
    print("did encode", file=sys.stderr)
    return key 

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
    if args.key_count is not None:
        #open file key.txt for writing
        # f_key = open("key.txt", "w+")
        key_chars = int(args.key_count)
        try:
            with open("key.txt", "w+") as f_key:
                for i in range(key_chars):
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
            print("oops...error")
        #generate plaintext file to hold original message for encryption
        try:
            with open("plaintext.txt", "r") as f_plaintext:
                plaintext_data = f_plaintext.read()
        except FileNotFoundError as err:
            print(err)
        # key_chars = int(args.key_count)
        #generate random number to use as index to capture a char from global alpha var
        # for i in range(key_chars):
        #     #generate random number 
        #     rand_num = random.randrange(27)
        #     #use random number as index and extract char from alpha variable to write to key file 
        #     #this will create the key to encode the original message
        #     rand_char = alpha[rand_num]
        #     f_key.write(rand_char)
        #add newline char
        # 
        f_key.close()
        f_plaintext.close()
    else:
        try:
            with open("key.txt", "r") as file1:
                file1 = file1.read()
        except FileNotFoundError as err:
            print(err)

        # if args.encode_file is not None:
        #     # print("demitri first", file=sys.stderr) #printiin to stdout but with pipe goes to decoder aka stdin of decoder
        #     ###plaintext redirected from cat plaintext.txt###
        #     #get len of key file
        #     #generate ciphertext by calling fx passing key, plaintext
        #     ciphertext = encode(key)
        #     sys.stdout.write(ciphertext)
        # if args.decode_file is not None:
        #     # print("demitri", file=sys.stderr)
        #     new_var = sys.stdin.read()
        #     #generate new_plaintext by passing key and ciphertext to appropriate fx
        #     new_plaintext = decode(key)
        #     sys.stdout.write(new_plaintext)
        # file1.close()
           
    print(args, file=sys.stderr)
    
    

if __name__ == "__main__":
    main()

