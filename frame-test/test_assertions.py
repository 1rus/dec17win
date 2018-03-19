from assertions import Assertions as a
import pytest


@pytest.mark.incremental
def test_assert_equal():
    result = a("", []).assert_equal(1, 1)
    print(result)


def test_verify_equal():
    result = a("", []).verify_equal(1, 2, "verify failed 1 <> 2")
    print(result)


def test_assert_not_equal():
    result = a("", []).assert_not_equal(1, 2)
    print(result)
