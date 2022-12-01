from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    result = encrypt_message("xablau", 3)
    assert result == "bax_ual"

    result = encrypt_message("xablau", 8)
    assert result == "ualbax"

    with pytest.raises(TypeError):
        encrypt_message("xablau", "8")
        encrypt_message(5, 3)
        encrypt_message(3, "8")
