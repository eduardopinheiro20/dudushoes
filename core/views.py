# coding=utf-8

#Toda view no django tem que retornar um obejto httpResponse

from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import View, TemplateView, CreateView
from django.contrib.auth import get_user_model
from django.contrib import messages

from .forms import ContactForm


User = get_user_model()

class IndexView(TemplateView):

    template_name = 'index.html'


class AboutView(TemplateView):
    template_name = 'about.html'

class ModelosView(TemplateView):
    template_name = 'modelos.html'

class TecnologiaView(TemplateView):
    template_name = 'tecnologi.html'





about = AboutView.as_view()
index = IndexView.as_view()
modelos = ModelosView.as_view()
tecnologi = TecnologiaView.as_view()


def contact(request):
    success = False
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.send_mail()
        success = True
    elif request.method == 'POST':
        messages.error(request, 'Formulário inválido')
    context = {
        'form': form,
        'success': success
    }
    return render(request, 'contact.html', context)
