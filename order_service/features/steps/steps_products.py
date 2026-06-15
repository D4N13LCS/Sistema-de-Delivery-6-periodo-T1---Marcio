from behave import given, when, then

from products.models import Produto

@given("não existem produtos cadastrados")
def step_impl(context):
    from products.models import Produto
    Produto.objects.all().delete()


@when("acesso a API de produtos")
def step_impl(context):
    context.response = context.client.get("/api/products/")


@then("devo receber uma lista vazia")
def step_impl(context):
    assert context.response.status_code == 200
    assert context.response.json() == []

@given("existem produtos cadastrados")
def step_existem_produtos_cadastrados(context):
    Produto.objects.create(
        nome="X-Burger",
        preco=20,
        descricao="Hambúrguer de teste",
        imagem="https://teste.com/xburger.jpg",
    )

    Produto.objects.create(
        nome="X-Salada",
        preco=18,
        descricao="Outro produto de teste",
        imagem="https://teste.com/xsalada.jpg",
    )


@when("acesso a API de produtos")
def step_acesso_api_produtos(context):
    context.response = context.client.get("/api/products/")


@then("devo receber uma lista de produtos")
def step_recebo_lista_produtos(context):
    assert context.response.status_code == 200

    data = context.response.json()

    assert isinstance(data, list)
    assert len(data) >= 2

    primeiro = data[0]

    assert "id" in primeiro
    assert "nome" in primeiro
    assert "preco" in primeiro