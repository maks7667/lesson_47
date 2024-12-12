from django.urls import path
from . import views
from .views import BBLoginView, profile

app_name = 'main'


urlpatterns = [
    path('accounts/login/', BBLoginView.as_view(), name='login'),

    path('accounts/profile/', profile, name='profile'),
    path('<str:page>', views.other_page, name='other'),
    path('', views.index, name='index')
]
