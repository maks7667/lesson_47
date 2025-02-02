from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.template.exceptions import TemplateDoesNotExist
from django.template.loader import get_template

def index(request):
    return render(request, 'main/index.html')

def other_page(request, page):
    try:
        template  = get_template('main/' + page + '.html')
    except TemplateDoesNotExist:
        return Http404
    return HttpResponse(template.render(request=request))

class BBLoginView(LoginView):
        template_name = 'main/login.html'

@login_required
def profile(request):
    return render(request, 'main/profile.html')

