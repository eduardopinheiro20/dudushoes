"""

listas de URLS, caminhos possiveis para identificar


"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.views.static import serve as serve_static
from django.conf.urls.static import static
from django.contrib.auth.views import login, logout

from core import views


urlpatterns = [ #Listas de urls-  Caminhos paa a minha para aplicação
    # ^ abre o caminho, $ fecha o caminho
    url(r'^$', views.index, name='index'),
    url(r'^contato/$', views.contact, name='contact'),
    url(r'^sobrenos/$', views.about, name='about'),
    url(r'^modelos/$', views.modelos, name='modelos'),
    url(r'^tecnologi/$', views.tecnologi, name='tecnologi'),
    url(r'^entrar/$', login, {'template_name': 'login.html'}, name='login'),
    url(r'^sair/$', logout, {'next_page': 'catalog:shop'}, name='logout'),
    url(r'^catalogo/', include(('catalog.urls', 'catalog'), namespace='catalog')),
    url(r'^conta/', include(('accounts.urls', 'accounts'), namespace='accounts')),
    url(r'^compras/', include(('checkout.urls', 'checkout'), namespace='checkout')),
    url(r'^paypal/', include('paypal.standard.ipn.urls')),

    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
