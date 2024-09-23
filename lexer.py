import tokens  # Importa o módulo de tokens
from tokens import Token  # Importa a classe Token do módulo de tokens

# Classe Lexer para analisar o texto
class Lexer:
    def __init__(self, texto):
        self.texto = texto  # O texto que será analisado
        self.index = 0  # Posição atual no texto
        self.caractere_atual = None  # Caractere atual que estamos analisando
        self.avancar()  # Chama o método para avançar para o primeiro caractere

    def avancar(self):
        # Move para o próximo caractere
        if self.index < len(self.texto):
            self.caractere_atual = self.texto[self.index]  # Atualiza o caractere atual
            self.index += 1  # Avança o índice para o próximo caractere
        else:
            self.caractere_atual = None  # Se não houver mais caracteres, define como None

    def obter_tokens(self):
        tokens_lista = []  # Inicializa uma lista vazia para armazenar os tokens

        while self.caractere_atual is not None:  # Enquanto houver caracteres a serem processados

            if self.caractere_atual.isspace():  # Se o caractere atual for um espaço em branco
                self.avancar()  # Avança para o próximo caractere

            elif self.caractere_atual.isdigit() or self.caractere_atual == ".":  
                tokens_lista.append(self.obter_numero())  # Adiciona o número à lista de tokens

            elif self.caractere_atual == "+":  # Se o caractere atual for o operador de adição
                self.avancar()  # Avança para o próximo caractere
                tokens_lista.append(Token(tokens.SOMA))  # Adiciona o token SOMA à lista

            elif self.caractere_atual == "-":  # Se o caractere atual for o operador de subtração
                self.avancar()  # Avança para o próximo caractere
                tokens_lista.append(Token(tokens.SUBTRAÇÃO))  # Adiciona o token SUBTRAÇÃO à lista

            elif self.caractere_atual == "*":  # Se o caractere atual for o operador de multiplicação
                self.avancar()  # Avança para o próximo caractere
                tokens_lista.append(Token(tokens.MULTIPLICAÇÃO))  # Adiciona o token MULTIPLICAÇÃO à lista

            elif self.caractere_atual == "/":  # Se o caractere atual for o operador de divisão
                self.avancar()  # Avança para o próximo caractere
                tokens_lista.append(Token(tokens.DIVISÃO))  # Adiciona o token DIVISÃO à lista

            elif self.caractere_atual == "(":  # Se o caractere atual for o parêntese esquerdo
                self.avancar()  # Avança para o próximo caractere
                tokens_lista.append(Token(tokens.PAR_ESQUERDO))  # Adiciona o token PARENTESE_ESQUERDO à lista

            elif self.caractere_atual == "%":  # Se o caractere atual for o operador de porcentagem
                self.avancar()  # Avança para o próximo caractere
                tokens_lista.append(Token(tokens.PERCENTAGEM))  # Adiciona o token PORCENTAGEM à lista

            elif self.caractere_atual == ")":  # Se o caractere atual for o parêntese direito
                self.avancar()  # Avança para o próximo caractere
                tokens_lista.append(Token(tokens.PAR_DIREITO))  # Adiciona o token PARENTESE_DIREITO à lista

            else:  # Se o caractere não for reconhecido
                raise RuntimeError("Caractere ilegal -> " + self.caractere_atual)  # Lança um erro indicando o caractere ilegal

        return tokens_lista  # Retorna a lista de tokens encontrados

    def obter_numero(self):
        numero_str = self.caractere_atual  # Começa a construir o número
        ponto_count = 0  # Contador de pontos
        self.avancar()  # Avança para o próximo caractere

        while self.caractere_atual is not None and (self.caractere_atual.isdigit() or self.caractere_atual == "."):
            if self.caractere_atual == ".":
                ponto_count += 1
                if ponto_count > 1:  # Mais de um ponto não é permitido
                    break

            numero_str += self.caractere_atual  # Adiciona o caractere ao número
            self.avancar()  # Avança para o próximo caractere

        if numero_str[0] == ".":
            numero_str = "0" + numero_str  # Adiciona 0 antes do ponto se necessário

        if numero_str[-1] == ".":
            numero_str += "0"  # Adiciona 0 depois do ponto se necessário

        return Token(tokens.NUMERO, float(numero_str))  # Retorna um token do tipo NUMBER
