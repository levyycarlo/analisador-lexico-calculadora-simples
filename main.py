from lexer import Lexer  # Importa a classe Lexer do módulo lexer, responsável por analisar o texto.
import sys  # Importa o módulo sys para manipulação do sistema, como captura de erros.

def main():
    # Loop infinito para permitir a entrada contínua de expressões pelo usuário.
    while True:
        try:
            text = input("calc > ")  # Solicita ao usuário que insira uma expressão matemática.
            
            # Verifica se a entrada do usuário é uma string vazia.
            
            if text.strip() == "":
                continue  # Se a entrada for vazia, continua para a próxima iteração do loop.

            # Cria uma nova instância do Lexer com o texto inserido pelo usuário.
            lexer = Lexer(text)  
            
            # Chama o método obter_tokens do lexer para analisar o texto e obter a lista de tokens.
            tokens = lexer.obter_tokens()  

            # Itera sobre a lista de tokens gerados.
            for token in tokens:  
                print(token)  # Imprime cada token no console.

        # Captura um erro específico de execução (RuntimeError) e imprime a mensagem de erro.
        except RuntimeError as e:  
            print(f"error: {e.args[0]}", file=sys.stderr)  # Exibe a mensagem de erro no console de erros padrão.
        
        # Captura qualquer outro erro inesperado e imprime uma mensagem de erro genérica.
        except Exception as e:  
            print(f"Unexpected error: {e}", file=sys.stderr)  # Exibe a mensagem de erro genérica.

# Verifica se o script está sendo executado diretamente (não importado como módulo).
if __name__ == "__main__":  
    main()  # Chama a função main para iniciar o programa.
