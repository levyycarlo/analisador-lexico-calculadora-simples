import re


PALAVRAS_CHAVE = {
    "começar_partida": "INÍCIO",
    "fim_partida": "END",
    "se_der": "IF",
    "senão": "ELSE",
    "se_não_der": "ELIF",
    "tenta_aí": "TRY",
    "pega_a_rodada": "EXCEPT",
    "pausar": "PAUSE",
    "continuar": "CONTINUE",
    "driblar": "DRIBBLE",
    "passar": "PASS",
    "chutar": "KICK",
    "marcar_gol": "SCORE_GOAL",
    "enquanto": "WHILE",
    "para_cada": "FOR",
    "quebra": "BREAK",
    "continua_jogo": "CONTINUE",
    "ou_isso": "OR",
    "e": "AND",
    "não_da": "NOT",
    "time_de_reserva": "PUBLIC",
    "time_titular": "PRIVATE",
    "time": "CLASS",
    "jogador": "VARIABLE",
    "goleiro": "GOALKEEPER",
    "escalação": "LIST",
    "tática_do_time": "DICT",
    "narrar": "PRINT",
    "recebe_bola": "INPUT",
}


TOKEN_REGEXES = [
    (r'#.*', None),  
    (r'\b(' + '|'.join(PALAVRAS_CHAVE.keys()) + r')\b', 'PALAVRA_CHAVE'), 
    (r'"([^"\\]*(\\.[^"\\]*)*)"', 'STRING'), 
    (r"'([^'\\]*(\\.[^'\\]*)*)'", 'STRING'),  
    (r':', 'DOIS_PONTOS'),  
    (r'=', 'OPERADOR_ATRIBUICAO'),  
    (r'>=', 'MAIOR_IGUAL'), 
    (r'<=', 'MENOR_IGUAL'),  
    (r'>', 'MAIOR'),  
    (r'<', 'MENOR'), 
    (r'==', 'IGUAL'), 
    (r'!=', 'DIFERENTE'),  
    (r'~', 'OPERADOR_TIL'),  
    (r'[a-zA-Z0-9_ãáâàäçêéíóôõúü]+', 'IDENTIFICADOR'),  
    (r'\d+\.\d+', 'NUMERO_REAL'),  
    (r'\d+', 'NUMERO_INTEIRO'),  
    (r'[\{\};,]', 'PONTUACAO'), 
    (r'\+', 'OPERADOR_SOMA'),  
    (r'-', 'OPERADOR_SUBTRACAO'),  
    (r'\*', 'OPERADOR_MULTIPLICACAO'),  
    (r'\/', 'OPERADOR_DIVISAO'),  
    (r'%', 'OPERADOR_PORCENTAGEM'),  
    (r'\(', 'PAR_ESQUERDO'), 
    (r'\)', 'PAR_DIREITO'),  
    (r'\s+', None),  
]


class Token:
    def __init__(self, tipo, valor, linha):
        self.tipo = tipo       
        self.valor = valor      
        self.linha = linha      

    def __repr__(self):
        
        if self.valor is not None:
            return f"{self.tipo}: {self.valor} (linha: {self.linha})"
        return self.tipo
