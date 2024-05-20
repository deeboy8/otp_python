import argparse
import sys
import random
import time
import string

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "

def get_index_value(character):
    for i in range(len(alpha)):
        if character == alpha[i]:
            return i 

#based on flag passed (either encoding or decoding) will get sum or subtract value of key[char] and ciphertext[char]/plaintext[char]
#will use value to collect correct char from alphabet to encrypt/decrypt 
def generate_encrypted_or_decrypted_message(key, data, count, flag):
    buffer = []
    for i in range(len(data)):
        key_char_index_value = get_index_value(key[i])
        data_char_index_value = get_index_value(data[i])

        #based on flag will subtract or add data char to key char value
        #if encryption, key will be added to data message
        #if decrytping, key will be substacted from data message
        if flag == 'e':
            sum_of_chars = (data_char_index_value + key_char_index_value) % len(alpha)
        if flag == 'd':
            sum_of_chars = (data_char_index_value - key_char_index_value) % len(alpha)
        char_for_message = alpha[sum_of_chars] 
        buffer.append(char_for_message)

    resultant_string = ''.join(buffer)

    return resultant_string

#pass ciphertext data for decrytped message
def decode(alpha, key, ciphertext, ciphertext_len):
    result = generate_encrypted_or_decrypted_message(key, ciphertext, ciphertext_len, 'd')

    return result 

#pass plaintext data for encryption
def encode(alpha, key, plaintext, plaintext_count):
    result = generate_encrypted_or_decrypted_message(key, plaintext, plaintext_count, 'e')

    return result

def main():
    #generate parser and fill with appropriate command line arguments
    parser = argparse.ArgumentParser(prog='otp',
                                    description='otp (one time pad) is a program which recieves a message, either plaintext or encrypted, and performs encryption or decryption using a random key',
                                    epilog='thanks for using my %(prog)s program :)')    
    #otp arguments
    parser.add_argument('-ver', '--version', default= 1, type=bool)
    #grouping command keywords together
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-encode', action='store_true', dest='encode', help="command to initiate encoding of plaintext to ciphertext")
    group.add_argument('-keygen', action='store_true', dest='keygen', help="command to generate a key for encoding and decodying message")
    group.add_argument('-decode', action='store_true', dest='decode', help='command to initiate decodeding of messaage') #convert this to take decode.txt file
    #arguments for key generation
    parser.add_argument('-k', '--key-file', dest = 'key_text', default='key.txt', help = 'file to be generated opened') #convert this to key file 
    parser.add_argument('-l', '--length', help = 'count of chars to generate for key file to hold') #convert this to key file 
    parser.add_argument('-s', '--seed', dest='seed_value', help='provide a value to use to seed the random generator: for debuggging purposes')
    #arguments for encoding and decoding
    parser.add_argument('-i', '--input_file', dest = 'input_file',  help = 'name of file to be used containing message for encoding') #convert this to take encode.txt file
    parser.add_argument('-t', '--text', dest='cl_text', help = 'specify input text directly from command line for encoding') 
    parser.add_argument('-T', '--file_text', dest='file_text', help = 'the message to be encoded') 
    parser.add_argument('-o', '--output_file', dest='output_file', help = 'filename to be used for encoded message')
    #file arguments
    parser.add_argument('-v', '--verbose', help='provide greater depth of help test')
    args = parser.parse_args()
    print(args)
    
    #beginning of UI/CL interface
    #generate key file consisting of random chars for encoding and decoding plaintext and ciphertext
    if args.keygen: # and (args.encode is None or args.decode is None):
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
        # plaintext_len = len(str(args.cl_text))
        #generate plaintext file to hold original msg
        #will be used in comparing orginal msg with decoded msg using linux diff cmd
        if args.cl_text is not None and args.file_text is not None:
            print("usage error: only one importation of plaintext allowed", file=sys.stderr)
        if args.cl_text is not None or args.file_text is not None:
            try:
                if args.cl_text is not None and args.input_file is not None and args.file_text is None:
                    #if -p flag used will pull text directly from command line from user
                    #will write text to new file created
                    with open(args.input_file, "w+") as f_plaintext:
                        f_plaintext.write(args.cl_text)
                        f_plaintext.seek(0)
                        data = f_plaintext.read()
                        pt_data = data.upper()
                        # sys.stdout.write(pt_data)
                #will open text file and read into stdout handle for redirection on command line
                elif args.file_text is not None and (args.cl_text is None and args.input_file is None):
                    with open(args.file_text, "r") as f_plaintext:
                        data = f_plaintext.read()
                        pt_data = data.upper()
            except FileNotFoundError as err:
                print(err)
        if args.keygen is True or args.encode is True:
            plaintext_len = len(pt_data)
        #generate encoding of original msg using key file and original plaintext file
        #this will create the ciphertext file
        if args.encode is not None and (args.keygen is False and args.decode is False):
            #generate ciphertext by calling fx passing key, plaintext
            ciphertext = encode(alpha, key_data, pt_data, plaintext_len)
            cp_text = len(ciphertext)
            
            try:
                with open(args.output_file, 'w+') as cipher:
                    cipher.write(ciphertext)
                    sys.stdout.write(ciphertext)
            except FileNotFoundError as err:
                print(err)
            sys.stdout.write(ciphertext)
        #generate decoded original msg using key file and the ciphertext file
        #this will create the original msg store in the variable new_plaintext
        if args.decode is True and (args.keygen is False and args.encode is False):
            #open ciphertext file to import encoded message for decoding
            # if args.input_file is not None: #True: 
            sys.stdin.read()
            try:
                with open(args.input_file, "r") as decode_file:
                    cp_text = decode_file.read()
                    cp_text_len = len(cp_text)
            except:
                print(err)
            #generate new_plaintext by passing key and ciphertext to appropriate fx
            decoded_plaintext = decode(alpha, key_data, cp_text, cp_text_len)
            try:
                with open(args.output_file, 'w+') as new_plaintext:
                    new_plaintext.write(decoded_plaintext)
            except FileNotFoundError as err:
                print(err)
            # sys.stdout.write(decoded_plaintext)
    
if __name__ == "__main__":
    main()