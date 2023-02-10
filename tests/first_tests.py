from app import Calculator


class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_calculate_correctly(self):
        assert self.calc.multiply(self, 2, 2) == 4

    def testf_division(self):
        assert self.calc.division(self, 20, 2) == 10

    def testf_subtraction(self):
        assert self.calc.subtraction(self, 20, 2) == 18

    def testf_adding(self):
        assert self.calc.adding(self, 20, 2) == 22
