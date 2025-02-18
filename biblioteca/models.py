from django.db import models

class Livro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=200)
    ano_publicacao = models.IntegerField()
    
    
    def __str__(self):
        return f'{self.titulo} ({self.autor})'
    
    
class Aluno(models.Model):
    nome = models.CharField(max_length=200)
    matricula = models.IntegerField()
    curso = models.CharField(max_length=100)
    
    def __str__(self):
        return f'{self.nome} - {self.matricula}'
    
class Emprestimo (models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.PROTECT)
    livro = models.ForeignKey(Livro, on_delete=models.PROTECT)
    data_emprestimo = models.DateField()
    data_devolucao = models.DateField()
    
    def __str__(self):
        return f'{self.livro.titulo} - {self.aluno.nome}'