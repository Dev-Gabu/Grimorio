from django.contrib import admin
from django.urls import path, include
from grimorio.views import Login, Logout

urlpatterns = [
    path('', Login.as_view(), name='index'),
    path('admin/', admin.site.urls),
    path('logout/', Logout.as_view(),name='logout'),
    path('item/', include('itens.urls'), name='itens'),
    path('ficha/',include('fichas.urls'), name="fichas")
]
