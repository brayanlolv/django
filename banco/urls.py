from app_dat_banco import views 
from django.contrib import admin
from django.urls import path

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('',views.home,name='home'),

    path('cadastro/',views.cadastro_tela,name='cadastro_tela'),

    path('cartao/',views.cartao,name='cartao_tela'),

    path('cadastro_submit/',views.cadastro_submit,name='cadastro_submit'),

    path('investimentos/',views.investimento_tela,name='investimento_tela'),
]
