from django.shortcuts import redirect, render
from pools.models import Company


def index(request):
    companys = Company.objects
    content = {'companys': companys}
    return render(request, 'dover.html', content)