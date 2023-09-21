import re
from validate_docbr import CPF

def cpf_valido(cpf):
        """Inclusão de validação a partir do serializer"""
        cpftool = CPF()
        return cpftool.validate(cpf)  


def nome_valido(nome):
     return nome.isalpha()
         
def rg_valido(rg):
        """Inclusão de validação a partir do serializer"""
        return len(rg) == 9

def celular_valido(celular):
        """Verifica de celular é válido (00 00000-0000)"""
        
        modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'
        return re.findall(modelo, celular)
       