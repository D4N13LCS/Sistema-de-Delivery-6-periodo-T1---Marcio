from django.test import Client

def before_all(context):
    context.client = Client()
    context.base_url = "http://127.0.0.1:8000"