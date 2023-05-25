import re
from token import Token
from symbol import Symbol


class Lexer:

    def __init__(self, input_txt):
        self.input_txt = input_txt
        self.tokens = list()
        self.curr_index = 0
        self.lexeme = ''

    def start_analysis(self):
        # This method will commence the lexer from the main
        # Will end once the entire file is scanned

        while self.curr_index < len(self.input_txt):
            self.lex()

    def lex(self):
        if self.input_txt[self.curr_index].isalpha():
            self.tokenize_str()
            print('Was I here')
        elif self.input_txt[self.curr_index].isnumeric():
            pass
        else:
            pass

    def tokenize_str(self):
        regex = '([a-zA-Z]|_)([a-zA-Z]|[0-9]|_)*'
        self.lexeme += self.input_txt[self.curr_index]
        window_start = self.curr_index
        self.curr_index += 1
        while self.curr_index < len(self.input_txt):
            if not re.match(regex, self.input_txt[window_start:self.curr_index]):
                token = Token(self.lexeme, Symbol.IDENT, 1, 1)
                self.tokens.append(token)
                break
            self.lexeme += self.input_txt[self.curr_index]
            self.curr_index += 1
        print(self.tokens)
