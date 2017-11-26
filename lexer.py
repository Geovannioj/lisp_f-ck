
import ox 

lexer = [
    ('PARANTHESIS_OPENED', r'\('),
    ('PARANTHESIS_CLOSED', r'\)'),
    ('PLAIN_TEXT', r'[-a-zA-Z]+'),
    ('NUMBERS', r'\d+'),
    ('NEWLINE', r'\s+'),
    ('COMMENT', r';[^\n]*')
]

tokens = [
    'PARANTHESIS_OPENED',
    'PARANTHESIS_CLOSED',
    'PLAIN_TEXT',
    'NUMBERS',
    'NEWLINE',
    'COMMENT'
]

parser = ox.make_parser([
    ('atom : PLAIN_TEXT', lambda x: x),
    ('atom : NUMBERS', lambda x: X),
    ('block : PARANTHESIS_OPENED atom PARANTHESIS_CLOSED', lambda x, y, z: y),
    ('block : PARANTHESIS_OPENED PARANTHESIS_CLOSED'lambda x,y:'()'),
    ('exp : atom exp', lambda x, y: (x,) + y),
    ('exp : atom', lambda x: (x,)),
    ('atom : block', lambda x: x),   
], tokens)

#def parser():

