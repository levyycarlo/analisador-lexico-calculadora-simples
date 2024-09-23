# Definindo Tokens
NUMERO = "NUMERO"          # Token para números
SOMA = "SOMA"              # Token para o operador de adição
SUBTRAÇÃO = "SUBTRAÇÃO"    # Token para o operador de subtração
MULTIPLICAÇÃO = "MULTIPLICAÇÃO"  # Token para o operador de multiplicação
DIVISÃO = "DIVISÃO"        # Token para o operador de divisão
PERCENTAGEM = "PERCENTAGEM"  # Token para o operador de porcentagem
PAR_ESQUERDO = "PAR_ESQUERDO"  # Token para o parêntese esquerdo (  
PAR_DIREITO = "PAR_DIREITO"  # Token para o parêntese direito

# Classe que define o token
class Token:
    def __init__(self, tipo, valor=None):
        self.tipo = tipo  # Armazena o tipo do token (ex: PLUS, NUMBER)
        self.valor = valor  # Armazena o valor do token (ex: o número 5)

    # Representação do token para facilitar a visualização
    def __repr__(self):
        if self.valor is not None:  # Verifica se há um valor
            return f"{self.tipo}: {self.valor}"  # Retorna tipo e valor
        return self.tipo  # Retorna apenas o tipo se não houver valor
