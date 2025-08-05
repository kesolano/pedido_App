from django.urls import path
from .views import crear_pedido
from django.views.generic import TemplateView

urlpatterns = [
    path('', crear_pedido, name='crear_pedido'),
    path('pedido_exitoso/', TemplateView.as_view(template_name='app_Pedidos/pedido_exitoso.html'), name='pedido_exitoso'),
]
