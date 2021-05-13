from rest_framework import serializers
from .models import Curso, Avaliacao
from django.db.models import Avg

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

#validacao tem q comecar com validate_ e utilizar o nome declarado no fields
    def validate_avaliacao(self, valor):
        if valor <= 5:
            return valor
        raise serializers.ValidationError('A avaliação precisa ser um valor entre 1 e 5')


class CursoSerializer(serializers.ModelSerializer):
    # nested relationship(ideal para one to one - concatena informações)
    # avaliacoes = AvaliacaoSerializer(many=True, read_only=True)

    # Hyperliked Related Field(recomendado para api rest - cria link)
    # avaliacoes = serializers.HyperlinkedRelatedField(many=True,
    #                                                  read_only=True,
    #                                                  view_name='avaliacao-detail')

    # Primary Key Related Field(cria só com id relacionado)
    avaliacoes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    # para utilizar SerializerMethodField, é preciso de um método com
    # nome get_xxxx, onde xxx é o nome do campo do serializer(isso é padrão)
    media_avaliacoes = serializers.SerializerMethodField()
    class Meta:
        model = Curso
        fields = (
            'id',
            'titulo',
            'url',
            'criacao',
            'ativo',
            'avaliacoes',
            'media_avaliacoes'
        )

    def get_media_avaliacoes(self, obj):
        media = obj.avaliacoes.aggregate(Avg('avaliacao')).get('avaliacao__avg')

        if media is None:
            return 0
        return round(media * 2 ) / 2
