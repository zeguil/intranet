from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


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
    path('', include(router.urls)),
    path('', include('pages.urls')),
    path('login/', TokenObtainPairView.as_view()), # obter o token
    path('refresh/', TokenRefreshView.as_view()), # atualizar um token expirado
    # path('usuarios/', UsuariosList.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)