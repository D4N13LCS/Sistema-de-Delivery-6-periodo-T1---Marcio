from behave import given, when, then
from django.urls import reverse
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By


# ---------- TESTE VIEW (Django client) ----------
@given("que acesso a página de registro")
def step_impl(context):
    context.url = reverse("register")


@when("faço uma requisição GET")
def step_impl(context):
    context.response = context.client.get(context.url)


@then("o status code deve ser 200")
def step_impl(context):
    assert context.response.status_code == 200


# ---------- TESTE E2E (Selenium) ----------
@given("que estou na página de registro")
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get(f"{context.base_url}/register/")


@when('preencho username "{username}"')
def step_impl(context, username):
    context.driver.find_element(By.NAME, "username").send_keys(username)


@when('preencho password "{password}"')
def step_impl(context, password):
    context.driver.find_element(By.NAME, "password").send_keys(password)


@when('clico no botão "Criar Conta"')
def step_impl(context):
    context.driver.find_element(
        By.XPATH,
        "//button[contains(text(),'Criar Conta')]"
    ).click()


@then('devo ser redirecionado para "/login/"')
def step_impl(context):

    WebDriverWait(context.driver, 10).until(
        EC.url_contains("/login/")
    )

    assert "/login/" in context.driver.current_url

    context.driver.quit()