import pytest


def always_returns_true():
<<<<<<< HEAD
    print ("Hi, Rose! :D")
=======
    result = True
    return result
    
>>>>>>> 0002dc4604bd43ebd9c4deac0d2cc371149f8d42


def test_always_returns_true():
    assert always_returns_true()
