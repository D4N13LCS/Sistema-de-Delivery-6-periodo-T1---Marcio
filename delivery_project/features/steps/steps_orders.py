from behave import given, when, then
from orders.services.decorators import Lanche, ExtraQueijo, Bacon, Catupiry
from orders.services.payment_factory import PaymentFactory, PixPayment, CardPayment
from orders.services.delivery_strategy import EntregaNormal, EntregaExpressa
from orders.services.order_facade import OrderFacade

from django.contrib.auth.models import User
from accounts.models import Perfil
from products.models import Produto
from django.contrib.auth import login

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ---------- DECORATOR ----------
@given('um lanche X-Tudo custa {valor:d}')
def step_impl(context, valor):
    context.lanche = Lanche("X-Tudo", valor)


@when("adiciono queijo, bacon e catupiry")
def step_impl(context):
    context.lanche = ExtraQueijo(context.lanche)
    context.lanche = Bacon(context.lanche)
    context.lanche = Catupiry(context.lanche)


@then("o preço final deve ser {valor:d}")
def step_impl(context, valor):
    assert context.lanche.preco() == valor


# ---------- FACTORY ----------
@when('eu criar pagamento "{tipo}"')
def step_impl(context, tipo):
    context.pagamento = PaymentFactory.criar_pagamento(tipo)


@then("o tipo deve ser PixPayment")
def step_impl(context):
    assert isinstance(context.pagamento, PixPayment)


@then("o tipo deve ser CardPayment")
def step_impl(context):
    assert isinstance(context.pagamento, CardPayment)


# ---------- STRATEGY ----------
@given("uma entrega normal")
def step_impl(context):
    context.strategy = EntregaNormal()


@given("entrega expressa")
def step_impl(context):
    context.strategy = EntregaExpressa()


@when("valor do pedido é {valor:d}")
def step_impl(context, valor):
    context.resultado = context.strategy.calcular(valor)


@then("frete deve ser {valor:d}")
def step_impl(context, valor):
    assert context.resultado == valor


# ---------- FACADE ----------
@given("um usuário com saldo e um produto")
def step_impl(context):
    user = User.objects.create_user(username="teste", password="123")
    perfil = Perfil.objects.create(usuario=user, saldo=500)

    produto = Produto.objects.create(
        nome="X-Burger",
        preco=20,
        descricao="Teste",
        imagem="https://teste.com"
    )

    context.perfil = perfil
    context.produto = produto


@when("eu finalizar o pedido com pagamento pix")
def step_impl(context):
    context.pedido, context.resultado = OrderFacade.finalizar_pedido(
        context.perfil,
        context.produto,
        "",
        {"tipo": "normal", "taxa": 5, "pagamento": "pix"},
        20
    )


@then("o pedido deve ser criado com sucesso")
def step_impl(context):
    assert context.pedido.id is not None

# ---------- ACESSAR HISTÓRICO ----------
@when('acesso "/historico/"')
def step_impl(context):

    context.response = context.client.get(
        "/historico/"
    )

# ---------- HISTÓRICO ----------
@given("um usuário autenticado")
def step_impl(context):

    User.objects.create_user(
        username="teste",
        password="123456"
    )

    context.client.login(
        username="teste",
        password="123456"
    )


@when('acesso "/pedido/"')
def step_impl(context):

    context.response = context.client.get(
        "/pedido/"
    )


@then("o status code do pedido deve ser 200")
def step_impl(context):

    assert context.response.status_code == 200

# ---------- SELENIUM ORDER FLOW ----------
@given("usuário logado no sistema")
def step_impl(context):
    context.user = User.objects.create_user(
        username="teste",
        password="Senha@123"
    )
    context.driver = webdriver.Chrome()


@when("acesso página de pedido")
def step_impl(context):
    driver = context.driver
    driver.get(f"{context.live_server.url}/login/")

    driver.find_element(By.NAME, "username").send_keys("teste")
    driver.find_element(By.NAME, "password").send_keys("Senha@123")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    WebDriverWait(driver, 10).until(
        EC.url_changes(f"{context.live_server.url}/login/")
    )

    driver.get(f"{context.live_server.url}/pedido/")


@then('devo ver "Novo Pedido"')
def step_impl(context):
    WebDriverWait(context.driver, 10).until(
        EC.text_to_be_present_in_element((By.TAG_NAME, "body"), "Novo Pedido")
    )

    assert "Novo Pedido" in context.driver.page_source
    context.driver.quit()