from django.test import Client


def before_all(context):
    context.client = Client()