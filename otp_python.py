import argparse
import sys
import time

def decode(key):
    print("did decode", file=sys.stderr)
    return key 

def encode(key):
    print("did encode", file=sys.stderr)
    return key 

def main():
    #create and fill parser with appropriate arguments
    parser = argparse.ArgumentParser()
    #options for command line
    # add key generation information
    parser.add_argument('-k', '--key', dest = 'key_file', help = 'count of chars to generate for key file to hold')
    parser.add_argument('-e', '--encode', dest = 'encode_file', help = 'name of file to hold encoded text (plaintext text converted using key)')
    parser.add_argument('-d', '--decode', dest = 'decode_file', help='name of file holding decoded messaage (encoded text converted to plaintext)')
    parser.add_argument('-p', '--plaintext', help = 'the message to be encoded') 
    args = parser.parse_args()

    if args.key_file is not None:
        # open file key.txt file for writing
        f1 = open("key.txt", 'w+')
        alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
        # generate random number to use to capture random char from alpha var
        #pull value from alpha --> rand_char = alpha[value obtained from random numb generator]
        #write to opened file
        f1.write(alpha)
        #add newline char
        f1.close()
    else:
        file1 = open("key.txt", "r")
            #add exception
        key = file1.read()
                #add exception
        if args.encode_file is not None:
            print("demitri first", file=sys.stderr) #printiin to stdout but with pip goes to decoder aka stdin of decoder
            ###plaintext redirected from cat plaintext.txt###
            #read in key file
            #get len of key file
            #generate ciphertext by calling fx passing key, plaintext
            ciphertext = encode(key)
            f_encode = open("encode.txt", "w+")
            f_encode.write(ciphertext)
            f_encode.close()
        if args.decode_file is not None:
            time.sleep(.1)
            print("demitri", file=sys.stderr)
            new_var = sys.stdin.read()
            print(f"This is new_var: {new_var}", file=sys.stderr)
            ###ciphertext coming from stdout/redirection###
            #generate new_plaintext by passing key and ciphertext to appropriate fx
            new_plaintext = decode(key)
            f_decode = open("decode.txt", "w+")
            f_decode.write(new_plaintext)
            f_decode.close()
        file1.close()
        
        
    print(args, file=sys.stderr)
    
    

if __name__ == "__main__":
    main()

