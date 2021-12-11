

from typing import ValuesView, get_args
from django.views.generic import View
from django.shortcuts import render

class HomeView(View):
    def get(self,request,*args,**kwargs):
        return render(request, 'index.html', {})
        