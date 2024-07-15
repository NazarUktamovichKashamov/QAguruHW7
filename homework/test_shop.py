"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from homework.models import Product
from homework.models import Cart

@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)

@pytest.fixture
def cart():
    return Cart()


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        # TODO напишите проверки на метод check_quantity
        assert product.check_quantity(1) is True
        assert product.check_quantity(356) is True
        assert product.check_quantity(999) is True
        assert product.check_quantity(1000) is True
        assert product.check_quantity(1001) is False
        assert product.check_quantity(9458) is False


    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        product.buy(999)
        assert product.check_quantity(1) is True
        assert product.check_quantity(2) is False

    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        with pytest.raises(ValueError):
            product.buy(1001)



class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """
    def test_add_product_positive(self, cart, product):
        cart.add_product(product, 50)
        assert cart.products[product] == 50


    def test_add_product_zero(self, cart, product):
        cart.add_product(product, 0)
        assert cart.products[product] == 0


    def test_add_product_too_much(self, cart, product):
        cart.add_product(product, 123456789)
        assert cart.products[product] == 123456789


    def test_remove_product_positive(self, cart, product):
        cart.add_product(product, 50)
        cart.remove_product(product, 50)
        assert product not in cart.products


    def test_remove_product_more_than_in_cart(self, cart, product):
        cart.add_product(product, 50)
        cart.remove_product(product, 400)
        assert product not in cart.products


    def test_remove_product_with_remain(self, cart, product):
        cart.add_product(product, 50)
        cart.remove_product(product, 40)
        assert cart.products[product] == 10


    def test_clear_cart_positive(self, cart, product):
        cart.add_product(product, 50)
        cart.clear()
        assert product not in cart.products


    def test_clear_cart_when_it_already_has_been_cleared(self, cart, product):
        cart.add_product(product, 50)
        cart.remove_product(product, 50)
        cart.clear()
        assert product not in cart.products





