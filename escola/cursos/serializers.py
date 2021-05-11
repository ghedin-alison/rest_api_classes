from rest_framework import serializers
from .models import Curso, Avaliacao


class AvaliacaoSerializer(serializers.ModelSerializer):

    class Meta:
        extra_kwargs = {
            'email': {'write_only': True}
        } # configuração para não permitir a
          # disponibilizacao da info de email a usuarios
        model = Avaliacao
        fields = (
            'id',
            'curso',
            'nome_avaliador',
            'email',
            'comentario',
            'avaliacao',
            'criacao',
            'ativo'
        )


class CursoSerializer(serializers.ModelSerializer):
    # nested relationship(ideal para one to one - concatena informações)
    # avaliacoes = AvaliacaoSerializer(many=True, read_only=True)

    # Hyperliked Related Field(recomendado para api rest - cria link)
    # avaliacoes = serializers.HyperlinkedRelatedField(many=True,
    #                                                  read_only=True,
    #                                                  view_name='avaliacao-detail')

    # Primary Key Related Field(cria só com id relacionado)
    avaliacoes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Curso
        fields = (
            'id',
            'titulo',
            'url',
            'criacao',
            'ativo',
            'avaliacoes'
        )