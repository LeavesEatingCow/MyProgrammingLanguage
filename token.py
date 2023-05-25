class Token:

    def __init__(self, lexeme, code, row, column):
        self.lexeme = lexeme
        self.code = code
        self.row = row
        self.column = column

    def __str__(self):
        return f'{self.lexeme}'
