from lexer import Lexer


class Main:
    input_file = open('better_input.txt', 'rt')
    input_txt = input_file.read()
    lex = Lexer(input_txt)

    lex.start_analysis()
