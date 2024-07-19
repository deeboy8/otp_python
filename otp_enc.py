from otp_python import generate_encrypted_or_decrypted_message

# pass plaintext data for encryption
def encode(alpha, key, plaintext, plaintext_count):
    result = generate_encrypted_or_decrypted_message(
        key, plaintext, plaintext_count, "e"
    )

    return result