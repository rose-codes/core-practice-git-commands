import pytest


def always_returns_true():
    result = True
    return result
    


def test_always_returns_true():
    assert always_returns_true()
