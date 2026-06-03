from django.contrib.auth.models import User
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_realizar_pedido(live_server):

    User.objects.create_user(
        username="teste",
        password="Senha@123"
    )

    driver = webdriver.Chrome()

    try:

        driver.get(
            f"{live_server.url}/login/"
        )

        driver.find_element(
            By.NAME,
            "username"
        ).send_keys("teste")

        driver.find_element(
            By.NAME,
            "password"
        ).send_keys("Senha@123")

        driver.find_element(
            By.CSS_SELECTOR,
            "button[type='submit']"
        ).click()

        WebDriverWait(driver, 10).until(
            EC.url_changes(f"{live_server.url}/login/")
        )

        driver.get(
            f"{live_server.url}/pedido/"
        )

        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element(
                (By.TAG_NAME, "body"),
                "Novo Pedido"
            )
        )

        assert "Novo Pedido" in driver.page_source

    finally:

        driver.quit()