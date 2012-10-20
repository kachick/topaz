from ..base import BaseRuPyPyTest


class TestFloatObject(BaseRuPyPyTest):
    def test_add(self, space):
        w_res = space.execute("return 1.0 + 2.9")
        assert space.float_w(w_res) == 3.9

    def test_sub(self, space):
        w_res = space.execute("return 1.0 - 5.4")
        assert space.float_w(w_res) == -4.4

    def test_mul(self, space):
        w_res = space.execute("return 1.2 * 5.0")
        assert space.float_w(w_res) == 6.0

        w_res = space.execute("return 1.2 * 2")
        assert space.float_w(w_res) == 2.4

    def test_div(self, space):
        w_res = space.execute("return 5.0 / 2.0")
        assert space.float_w(w_res) == 2.5

    def test_neg(self, space):
        w_res = space.execute("return (-5.0)")
        assert space.float_w(w_res) == -5.0

        w_res = space.execute("return (-(4.0 + 1.0))")
        assert space.float_w(w_res) == -5.0

    def test_equal(self, space):
        w_res = space.execute("return 2.3 == 2.3")
        assert w_res is space.w_true
        w_res = space.execute("return 2.4 == 2.3")
        assert w_res is space.w_false

    def test_to_s(self, space):
        w_res = space.execute("return 1.5.to_s")
        assert space.str_w(w_res) == "1.5"

    def test_to_i(self, space):
        w_res = space.execute("return [1.1.to_i, 1.1.to_int]")
        assert self.unwrap(space, w_res) == [1, 1]
