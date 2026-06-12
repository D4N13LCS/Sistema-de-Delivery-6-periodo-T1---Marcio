from django.views.generic import ListView
from products.models import Produto


class HomeView(ListView):

    model = Produto

    template_name = 'home.html'

    context_object_name = 'produtos'

    paginate_by = 6

    ordering = ['nome']