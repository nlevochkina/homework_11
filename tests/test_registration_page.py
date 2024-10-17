import allure

from pages.registration_page import RegistrationPage
from data import users


@allure.title('Заполнение формы регистрации')
def test_fill_out_the_form():
    registration_page = RegistrationPage()
    with allure.step('Открываем форму'):
        registration_page.open_form()

    with allure.step('Заполняем форму'):
        registration_page.register_user(users.user)

    with allure.step('Проверяем соответствие полей в таблице'):
        registration_page.should_registered_user(users.user)
