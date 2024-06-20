from django.contrib import admin
from django.urls import path, include
from grimorio.views import Login, Logout
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', Login.as_view(), name='index'),
    path('admin/', admin.site.urls),
    path('logout/', Logout.as_view(),name='logout'),
    path('item/', include('itens.urls'), name='itens'),
    path('fichas/',include('fichas.urls'), name="fichas")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
