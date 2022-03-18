from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


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

schema_view = get_schema_view(
   openapi.Info(
      title="API Docs",
      default_version='v1',
      description="Intranet Produção",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@xyz.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('', include('pages.urls')),
    path('login/', TokenObtainPairView.as_view()), # obter o token
    path('refresh/', TokenRefreshView.as_view()), # atualizar um token expirado
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # path('usuarios/', UsuariosList.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

