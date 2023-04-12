import pytest

from calc import Calculator

class TestCalc:
    def setup(self):# сначала пишется метод setup
        self.calc = Calculator

    def test_adding_success(self):#тест который будет означать, что сложение прошло успешно
        assert self.calc.adding(self, 2, 2) == 4

    def test_adding_unsuccess(self):#сравниваем заведомо сломанный тест
        assert self.calc.adding(self, 2, 2) == 3

    def test_multiply(self):# тест\умножение
        assert self.calc.multiply(self, 3, 3) == 9

    def test_subtraction(self):# тест\вычитание
        assert self.calc.subtraction(self, 5, 2) == 3

    def test_zero_division(self):# тест деление на 0
        with pytest.raises(ZeroDivisionError):
            self.calc.division(self, 1, 0)

    def test_division(self):# тест \деление
        self.calc.division(self, 6, 3) == 2

    def teardown(self):
        print('Выполнение метода Teardown')
