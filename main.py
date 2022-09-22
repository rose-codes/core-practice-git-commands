import pytest


def always_returns_true():
    print ("Hi, Rose! :D")


def test_always_returns_true():
    assert always_returns_true()
