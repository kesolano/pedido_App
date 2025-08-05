from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import RedirectView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("pedidos/", include("app_Pedidos.urls")),
    path("", RedirectView.as_view(url="/pedidos/", permanent=False)),  # ← Añadido
]
