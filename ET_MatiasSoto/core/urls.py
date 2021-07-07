from django.urls import path
from .views import home
from .views import form_crear, form_mod
from .views import crud
from .views import form_del

urlpatterns =[
    path ('', home, name="home"),
    path('form_crear', form_crear, name="form_crear"),
    path('crud', crud, name="crud"),
    path('form_mod/<id>', form_mod, name="form_mod"),
    path('form_del/<id>', form_del, name="form_del"),
    
]