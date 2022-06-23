from django.shortcuts import render
from django.views.generic import TemplateView, DetailView

from core.models import Pet, Funcionario, Social


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['pets'] = Pet.objects.all()
        context['funcionarios'] = Funcionario.objects.all()
        context['sociais'] = Social.objects.all()
        return context

class DetalharPetView(DetailView):
    template_name = 'detalhar_pet.html'
    model = Pet


# Create your views here.
