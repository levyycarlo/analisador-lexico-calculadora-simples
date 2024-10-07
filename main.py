import sys
from lexer import Lexer

def imprimir_cabecalho():
    print("| %-15s | %-25s | %-5s |" % ("Lexema", "Token", "Linha"))
    print("|-----------------|-----------------|-------|")

def imprimir_token(token):
    # Ajustando a formatação para garantir alinhamento
    print("| %-15s | %-20s | %-5d |" % (token.valor.ljust(15), token.tipo.ljust(20), token.linha))

def main():
    if len(sys.argv) < 2:
        print("Uso: python main.py <nome_do_arquivo>")
        return

    nome_arquivo = sys.argv[1]

    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:  # Especificando a codificação UTF-8
            texto = arquivo.read()  # Lê o conteúdo do arquivo
            lexer = Lexer(texto)  # Cria uma instância do Lexer
            tokens = lexer.obter_tokens()  # Obtém os tokens

            imprimir_cabecalho()  # Imprime o cabeçalho da tabela
            for token in tokens:  # Itera sobre os tokens
                imprimir_token(token)  # Passa o objeto token para a função

    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
    except Exception as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()
