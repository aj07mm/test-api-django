from django.shortcuts import render
from django.contrib.auth import login
from django.views.generic import TemplateView


class Home(TemplateView):
    template_name = "home.html"


def login(request, hash):
    account = get_account_from_hash(hash)
    if not account.is_active:
        account.activate()
        account.save()
        user = account.user
        login(request, user)
