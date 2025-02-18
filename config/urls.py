from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from biblioteca.views import LivroViewSet, AlunoViewSet, EmprestimoViewSet

router = DefaultRouter()
router.register(r'livros', LivroViewSet)
router.register(r'alunos', AlunoViewSet)
router.register(r'emprestimos', EmprestimoViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
