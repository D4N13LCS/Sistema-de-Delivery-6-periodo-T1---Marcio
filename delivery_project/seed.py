import os
import django

os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE',
    'delivery_project.settings'
)

django.setup()

from accounts.models import Perfil
# from products.models import Produto
from django.contrib.auth.models import User

def run():

    produtos = [

        {
            "nome": "X-Burger",
            "preco": 22,
            "descricao": "Hambúrguer artesanal com carne e molho especial.",
            "imagem": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?q=80&w=1200"
        },

        {
            "nome": "X-Bacon",
            "preco": 28,
            "descricao": "Hambúrguer artesanal com bastante bacon crocante.",
            "imagem": "https://images.unsplash.com/photo-1550547660-d9450f859349?q=80&w=1200"
        },

        {
            "nome": "X-Tudo",
            "preco": 35,
            "descricao": "Hambúrguer completo com ovo, bacon e queijo.",
            "imagem": "https://images.unsplash.com/photo-1571091718767-18b5b1457add?q=80&w=1200"
        },

        {
            "nome": "X-Frango",
            "preco": 24,
            "descricao": "Sanduíche de frango empanado artesanal.",
            "imagem": "https://images.unsplash.com/photo-1606755962773-d324e0a13086?q=80&w=1200"
        },

        {
            "nome": "X-Calabresa",
            "preco": 26,
            "descricao": "Lanche de calabresa acebolada com queijo.",
            "imagem": "https://images.unsplash.com/photo-1525059696034-4967a8e1dca2?q=80&w=1200"
        },

        {
            "nome": "Hot Dog Especial",
            "preco": 20,
            "descricao": "Cachorro-quente completo com molho da casa.",
            "imagem": "https://images.unsplash.com/photo-1619740455993-9e612b1af08a?q=80&w=1200"
        }

    ]

    clientes = [

        {
            "nome": "Carlos",
            "saldo": 150
        },

        {
            "nome": "Marina",
            "saldo": 80
        },

        {
            "nome": "Fernanda",
            "saldo": 250
        },

        {
            "nome": "Lucas",
            "saldo": 40
        }

    ]

    # for produto in produtos:

    #     Produto.objects.update_or_create(
    #         nome=produto["nome"],
    #         defaults={
    #             "preco": produto["preco"],
    #             "descricao": produto["descricao"],
    #             "imagem": produto["imagem"]
    #         }
    #     )

    for cliente in clientes:

        usuario, created = User.objects.get_or_create(
            username=cliente["nome"]
        )

        if created:

            usuario.set_password("123")

            usuario.save()

        Perfil.objects.update_or_create(
            usuario=usuario,
            defaults={
                "saldo": cliente["saldo"],
                "endereco": "Endereço padrão"
            }
        )

    print("Seed executada com sucesso!")

if __name__ == "__main__":
    run()