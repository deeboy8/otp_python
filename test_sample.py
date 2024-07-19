# content of test_sample.py
def inc(x):
    return x + 1


def test_answer():
    assert inc(4) == 5



# #open file key.txt for writing
#         try:
#             with open("key.txt", "r") as f_key:
#                 key_data = f_key.read()
#         except FileNotFoundError as err:
#             print(err)
#         #generate plaintext file to hold original message for encryption
#         try:
#             with open("plaintext.txt", "r") as f_plaintext:
#                 plaintext_data = f_plaintext.read()
#         except FileNotFoundError as err:
#             print(err)
#         key_chars = int(args.key_count)
#         #generate random number to use as index to capture a char from global alpha var
#         for i in range(key_chars):
#             #generate random number 
#             rand_num = random.randrange(27)
#             #use random number as index and extract char from alpha variable to write to key file 
#             #this will create the key to encode the original message
#             rand_char = alpha[rand_num]
#             f_key.write(rand_char)