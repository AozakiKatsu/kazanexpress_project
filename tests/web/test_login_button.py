import allure

from tests_kazanexpress.pages.web.login_page import login_page


@allure.parent_suite('Web')
@allure.suite('Авторизация')
@allure.title(f"Проверка отображения поп-апа авторизации")
@allure.severity('Critical')
def test_login_button():
    login_page.open()

    login_page.click_login_button()

    login_page.should_pop_up_visible()
