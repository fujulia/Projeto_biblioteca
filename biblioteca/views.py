from rest_framework.viewsets import ModelViewSet
from .models import Livro, Aluno, Emprestimo
from .serializers import LivroSerializer, AlunoSerializer, EmprestimoSerializer

class LivroViewSet(ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
    
class AlunoViewSet(ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    
class EmprestimoViewSet(ModelViewSet):
    queryset = Emprestimo.objects.all()
    serializer_class = EmprestimoSerializer


