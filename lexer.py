
import ox 

lexer = [
    ('PARANTHESIS_OPENED', r'\('),
    ('PARANTHESIS_CLOSED', r'\)'),
    ('PLAIN_TEXT', r'[-a-zA-Z]+'),
    ('NUMBERS', r'\d+'),
    ('NEWLINE', r'\s+'),
    ('COMMENT', r';[^\n]*'),
]


#def parser():

