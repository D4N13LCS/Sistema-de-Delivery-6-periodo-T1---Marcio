from selenium import webdriver
from selenium.webdriver.common.by import By


def test_cadastro_usuario(live_server):

    driver = webdriver.Chrome()

    try:

        driver.get(
            f"{live_server.url}/register/"
        )

        driver.find_element(
            By.NAME,
            "username"
        ).send_keys(
            "usuario_teste"
        )

        driver.find_element(
            By.NAME,
            "password"
        ).send_keys(
            "Senha@123"
        )

        driver.find_element(
            By.XPATH,
            "//button[contains(text(),'Criar Conta')]"
        ).click()

        print(driver.current_url)
        print(driver.page_source)

        assert "/login/" in driver.current_url

    finally:

        driver.quit()