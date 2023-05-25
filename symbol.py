from enum import Enum


class Symbol(Enum):
    SEMICOLON = 0
    WHILE_CODE = 1
    LEFT_PAREN = 2
    RIGHT_PAREN = 3
    IF_CODE = 4
    ELSE_CODE = 5
    LEFT_CURLY = 6
    RIGHT_CURLY = 7
    ADD_OP = 8
    MINUS_OP = 9
    MULT_OP = 10
    DIV_OP = 11
    MOD_OP = 12
    EXP_OP = 13
    GREATER_THAN = 14
    LESS_THAN = 15
    GREATER_AND_EQUAL = 16
    LESS_AND_EQUAL = 17
    EQUALS = 18
    NOT_EQUALS = 19
    AND_OP = 20
    OR_OP = 21
    NOT_OP = 22
    IDENT = 23
    INT_LIT = 24
    FLOAT_LIT = 25
    CHAR_LIT = 26
    STRING_LIT = 27
    ASSIGN = 28
    COMMA = 29
    TRUE = 30
    FALSE = 31
    INT_TYPE = 32
    FLOAT_TYPE = 33
    STRING_TYPE = 34
    BOOL_TYPE = 35
    CHAR_TYPE = 36
    EOF = 37
