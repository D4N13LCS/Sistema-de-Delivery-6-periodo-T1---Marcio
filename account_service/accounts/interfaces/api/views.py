import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from accounts.application.use_cases.create_profile import CreateProfileUseCase
from accounts.application.use_cases.get_profile import GetProfileUseCase
from accounts.application.use_cases.update_address import UpdateAddressUseCase
from accounts.application.use_cases.credit_balance import CreditBalanceUseCase
from accounts.application.use_cases.debit_balance import DebitBalanceUseCase

from accounts.models import Perfil

@csrf_exempt
def create_profile(request):

    if request.method != "POST":
        return JsonResponse(
            {"erro": "Método não permitido"},
            status=405,
        )

    data = json.loads(request.body)

    perfil = CreateProfileUseCase().execute(data)

    return JsonResponse(
        {
            "usuario_id": perfil.usuario_id,
            "saldo": perfil.saldo,
            "endereco": perfil.endereco,
        },
        status=201,
    )


def get_profile(request, usuario_id):

    if request.method != "GET":
        return JsonResponse(
            {"erro": "Método não permitido"},
            status=405,
        )

    try:
        perfil = GetProfileUseCase().execute(usuario_id)

        return JsonResponse(
            {
                "usuario_id": perfil.usuario_id,
                "saldo": perfil.saldo,
                "endereco": perfil.endereco,
                "cartao_cadastrado": perfil.cartao_cadastrado,
                "numero_cartao": perfil.numero_cartao,
                "nome_cartao": perfil.nome_cartao,
                "validade_cartao": perfil.validade_cartao,
            }
        )

    except Perfil.DoesNotExist:

        return JsonResponse(
            {"erro": "Perfil não encontrado"},
            status=404,
        )
    
@csrf_exempt
def update_profile(request, usuario_id):

    if request.method != "PUT":
        return JsonResponse(
            {"erro": "Método não permitido"},
            status=405,
        )

    try:

        perfil = Perfil.objects.get(
            usuario_id=usuario_id
        )

    except Perfil.DoesNotExist:

        return JsonResponse(
            {"erro": "Perfil não encontrado"},
            status=404,
        )

    data = json.loads(request.body)

    perfil.endereco = data.get(
        "endereco",
        perfil.endereco,
    )

    perfil.saldo = data.get(
        "saldo",
        perfil.saldo,
    )

    perfil.numero_cartao = data.get(
        "numero_cartao",
        perfil.numero_cartao,
    )

    perfil.nome_cartao = data.get(
        "nome_cartao",
        perfil.nome_cartao,
    )

    perfil.validade_cartao = data.get(
        "validade_cartao",
        perfil.validade_cartao,
    )

    perfil.cartao_cadastrado = bool(
        perfil.numero_cartao
    )

    perfil.save()

    return JsonResponse(
        {"mensagem": "Perfil atualizado com sucesso"}
    )

@csrf_exempt
def delete_profile(request, usuario_id):

    if request.method != "DELETE":
        return JsonResponse(
            {"erro": "Método não permitido"},
            status=405,
        )

    try:

        perfil = Perfil.objects.get(
            usuario_id=usuario_id
        )

    except Perfil.DoesNotExist:

        return JsonResponse(
            {"erro": "Perfil não encontrado"},
            status=404,
        )

    perfil.delete()

    return JsonResponse(
        {"mensagem": "Perfil removido com sucesso"}
    )

@csrf_exempt
def credit_balance(request):

    if request.method != "POST":
        return JsonResponse(
            {"error": "Method not allowed"},
            status=405,
        )

    data = json.loads(request.body)

    perfil = CreditBalanceUseCase().execute(
        usuario_id=data["usuario_id"],
        valor=data["valor"],
    )

    return JsonResponse({
        "status": "success",
        "saldo": perfil.saldo,
    })


@csrf_exempt
def debit_balance(request):

    if request.method != "POST":
        return JsonResponse(
            {"error": "Method not allowed"},
            status=405,
        )

    data = json.loads(request.body)

    try:
        perfil = DebitBalanceUseCase().execute(
            usuario_id=data["usuario_id"],
            valor=data["valor"],
        )

        return JsonResponse({
            "status": "success",
            "saldo": perfil.saldo,
        })

    except ValueError as e:
        return JsonResponse(
            {"error": str(e)},
            status=400,
        )


@csrf_exempt
def update_address(request):

    if request.method != "POST":
        return JsonResponse(
            {"error": "Method not allowed"},
            status=405,
        )

    data = json.loads(request.body)

    perfil = UpdateAddressUseCase().execute(
        usuario_id=data["usuario_id"],
        endereco=data["endereco"],
    )

    return JsonResponse({
        "status": "success",
        "endereco": perfil.endereco,
    })