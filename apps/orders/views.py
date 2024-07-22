from django.shortcuts import redirect, render
from django.views.generic import TemplateView



def order_request(requet):
    print(requet.POST)

    return redirect('cinemas:index')
