from behave import given, when, then
from products.models import Produto
from selenium import webdriver


@given("existem 15 produtos")
def step_impl(context):
    for i in range(15):
        Produto.objects.create(
            nome=f"Produto {i}",
            preco=10,
            descricao="Teste",
            imagem="https://teste.com"
        )


@when("acesso a home")
def step_impl(context):
    context.response = context.client.get("/")


@then("o status code de products deve ser 200")
def step_impl(context):
    assert context.response.status_code == 200


@then("no máximo 6 produtos devem ser exibidos")
def step_impl(context):
    assert len(context.response.context["produtos"]) <= 6


# ---------- SELENIUM ----------
@when("acesso a página inicial")
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get(f"{context.base_url}/")


@then('devo ver "Cardápio"')
def step_impl(context):
    assert "Cardápio" in context.driver.page_source
    context.driver.quit()