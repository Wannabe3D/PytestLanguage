import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_store_buy_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(10)
    button = browser.find_element(By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket")
    assert button, "Кнопка добавления товара в корзину не найдена!"
    print(f'\nНайдена кнопка: "{button.text}"')
