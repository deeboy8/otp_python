import socket

from otp_enc import encode

HOST = "127.0.0.1" 
PORT = 65432

# function to obtain index value of char passed based on position in alphabet
# def get_index_value(character):
#     for i in range(len(alpha)):
#         if character == alpha[i]:
#             return i

#based on flag passed (either encoding or decoding) will get resultant arithmetic value of key[char] and ciphertext[char]/plaintext[char]
# will use value to collect correct char from alphabet to encrypt/decrypt based on resultant numeric value
# def generate_encrypted_or_decrypted_message(key, data, count, flag):
#     buffer = []
#     for i in range(count):
#         key_char_index_value = get_index_value(key[i])
#         data_char_index_value = get_index_value(data[i])

#         # based on flag will subtract or add data char to key char value
#         # if encryption, key will be added to data message
#         # if decrytping, key will be substacted from data message
#         if flag == "e":
#             sum_of_chars = (data_char_index_value + key_char_index_value) % len(alpha)
#         if flag == "d":
#             sum_of_chars = (data_char_index_value - key_char_index_value) % len(alpha)
#         char_for_message = alpha[sum_of_chars]
#         buffer.append(char_for_message)

#     resultant_string = "".join(buffer)

#     return resultant_string

# def encode_daemon():
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"successfuly connected by {addr}")
        while True:
            data = conn.recv(1024)
            #where code will perform encoding
            if not data:
                break
            #here is where the resultant ciphertext will be sent
            conn.sendall(data)
    
    # return 