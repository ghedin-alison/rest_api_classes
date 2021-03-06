from django.db import models


class Base(models.Model):
    """
        Entidade modelo
    """
    criacao = models.DateField(auto_now_add=True)
    atualizacao = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Curso(Base):
    """
        Entidade Curso
    """
    titulo = models.CharField(max_length=255)
    url = models.URLField(unique=True) #campo obrigatório e chave de unicidade

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        ordering = ['id']

    def __str__(self):
        return self.titulo


# Entidade Avaliação
class Avaliacao(Base):
     curso = models.ForeignKey(Curso, related_name='avaliacoes', on_delete=models.CASCADE)
     nome_avaliador = models.CharField(max_length=255)
     email = models.EmailField()
     comentario = models.TextField(blank=True, default='') #campo opcional
     avaliacao = models.DecimalField(max_digits=2, decimal_places=1)

     class Meta:
         verbose_name = 'avaliação'
         verbose_name_plural = 'avaliações'
         unique_together = ['email', 'curso'] # cada pessoa pode avaliar somente uma vez um curso
         ordering = ['id']

     def __str__(self):
         return f'{self.nome_avaliador} avaliou o curso {self.curso} com nota {self.avaliacao}'


