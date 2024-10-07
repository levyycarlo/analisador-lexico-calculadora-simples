import re  
import tokens  
from tokens import Token, TOKEN_REGEXES  


class Lexer:
    def __init__(self, texto):
        self.texto = texto 
        self.index = 0  
        self.caractere_atual = texto[self.index] if texto else None  
        self.linha_atual = 1  

    def avancar(self):
        
        self.index += 1
        self.caractere_atual = self.texto[self.index] if self.index < len(self.texto) else None

    def obter_tokens(self):
        tokens_lista = []  
        while self.caractere_atual is not None: 
            if self.caractere_atual == '\n':  
                self.linha_atual += 1  
                self.avancar()  
                continue  

            if self.caractere_atual.isspace(): 
                self.avancar()  
                continue  

            token, valor = self.match_regex()  
            if token:  
                
                tokens_lista.append(Token(token, valor, self.linha_atual))  
                
                self.index += len(valor) - 1
                self.avancar()  #
            else:
                raise RuntimeError(f"Caractere ilegal -> '{self.caractere_atual}' na linha {self.linha_atual} e posição {self.index}")  

        return tokens_lista  

    def match_regex(self):
       
        for regex, token_type in TOKEN_REGEXES:
            padrao = re.compile(regex)
            match = padrao.match(self.texto[self.index:])
            if match:
                valor = match.group(0)
                return token_type, valor  
        return None, None  
