from django.views.generic import TemplateView

from products.gateways.product_gateway import ProductGateway


class HomeView(TemplateView):

    template_name = "home.html"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        produtos = ProductGateway.listar()

        context["produtos"] = produtos[:6]

        return context
    