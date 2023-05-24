from lexer import Lexer


class Main:
    tokens = []
    input_file = open('input.txt', 'rt')
    input_txt = input_file.read()
    lex = Lexer(input_txt, tokens)

    


