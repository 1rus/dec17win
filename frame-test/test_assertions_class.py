from assertions import Assertions as a
import pytest


@pytest.mark.incremental
class Test_Assertions():
    def test_assert_equal(self):
        a("", []).assert_equal(1, 1)

    def test_verify_equal(self):
        a("", []).verify_equal(1, 2, "verify failed 1 <> 2")

    def test_assert_not_equal(self):
        a("", []).assert_not_equal(1, 2)
