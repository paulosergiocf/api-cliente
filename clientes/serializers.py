from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import *

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
    
    def validate(self, data):
        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError({'cpf':"O CPF informado é inválido"})

        if not nome_valido(data['nome']):
            raise serializers.ValidationError({'nome':"O nome não porde conter numeros"})
        
        if not rg_valido(data['rg']):
            raise serializers.ValidationError({'rg':"O rg deve ter 9 digitos"})

        if not celular_valido(data['celular']):
            raise serializers.ValidationError({'celular':"O celular deve seguir este modelo 00 00000-0000"})

        return data
   
    # def validate_celular(self, celular):
    #     """Inclusão de validação a partir do serializer"""
    #     if len(celular) < 11:
    #         raise serializers.ValidationError("O celular deve ter 11 digitos")
    #     return celular +