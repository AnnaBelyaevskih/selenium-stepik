import pytest

from pages.product_page import ProductPage


@pytest.mark.parametrize(
    "link",
    [
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
        pytest.param(
            "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
            marks=pytest.mark.xfail
        ),
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9",
    ]
)
def test_guest_can_add_product_to_basket(browser, link):

    page = ProductPage(browser, link)

    page.open()

    # Получаем данные товара ДО добавления в корзину
    product_name = page.get_product_name()
    product_price = page.get_product_price()

    # Добавляем товар в корзину
    page.add_to_basket()

    # Решаем промо-задание
    page.solve_quiz_and_get_code()

    # Проверяем результат
    page.should_be_success_message()
    page.should_be_product_name_in_success_message(product_name)
    page.should_be_price_in_success_message(product_price)