# content of test_sample.py
# def test_keygen(x):
#     return x + 1

from typer_otp.otp_typer import keygen

def test_keygen_length():
    assert keygen(4) == 8

# def test_answer_2(self):
#     assert inc(2) == 5