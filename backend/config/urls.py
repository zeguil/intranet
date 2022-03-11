from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken.views import obtain_auth_token


# Models ViewSet
from banner.viewsets import BannerViewSet
from comentario.viewsets import ComentarioViewSet
from audit.viewsets import AuditViewSet
from corporativo.viewsets import CorporativoViewSet
from emails.viewsets import EmailViewSet
from funcionario.viewsets import FuncionarioViewSet
from informativo.viewsets import InformativoViewSet
from ramal.viewsets import RamalViewSet
from setor.viewsets import SetorViewSet
from users.viewsets import UsuariosViewSet

from pages.views import Ramais,Info, Nivers, Noticias, Mural
router = routers.DefaultRouter()

# rotas
router.register(r'banner', BannerViewSet)
router.register(r'comentario', ComentarioViewSet)
router.register(r'audit', AuditViewSet)
router.register(r'corporativo', CorporativoViewSet)
router.register(r'email', EmailViewSet)
router.register(r'funcionario', FuncionarioViewSet)
router.register(r'informativo', InformativoViewSet)
router.register(r'ramal', RamalViewSet)
router.register(r'setor', SetorViewSet)
router.register(r'usuarios', UsuariosViewSet, basename='UsuariosViewSet')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', obtain_auth_token),
    path('', include(router.urls)),
    path('', include('pages.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)