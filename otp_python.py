import argparse

def encode(key):
    return "a"

def main():
    #create and fill parser with appropriate arguments
    parser = argparse.ArgumentParser()
    #options for command line
    # add key generation information
    parser.add_argument('-k', '--key', dest = 'key_file', default= 256, help = 'count of chars to generate for key file to hold')
    parser.add_argument('-e', '--encode', dest = 'encode_file', help = 'name of file to hold encoded text (plaintext text converted using key)')
    parser.add_argument('-d', '--decode', dest = 'decode_file', help='name of file holding decoded messaage (encoded text converted to plaintext)')
    parser.add_argument('-p', '--plaintext', help = 'the message to be encoded') 
    args = parser.parse_args()

    if args.key_file is not None:
        pass
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
        if args.encode_file is not None:
            ###plaintext redirected from cat plaintext.txt###
            #read in key file
            key = f1.read()
                #add exception
            #get len of key file
            #generate ciphertext by calling fx passing key, plaintext
            ciphertext = encode(key)
            print(ciphertext)

        if args.decode_file is not None:
            pass
        #open key file
                #add exception
            ###ciphertext coming from stdout/redirection###
            #generate new_plaintext by passing key and ciphertext to appropriate fx
        file1.close()
    print(args)
    print(args.plaintext)
    

if __name__ == "__main__":
    main()

