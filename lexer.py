
import ox
import click
import pprint



lexer = ox.make_lexer([
    ('PARANTHESIS_OPENED', r'\('),
    ('PARANTHESIS_CLOSED', r'\)'),
    ('PLAIN_TEXT', r'[-a-zA-Z]+'),
    ('NUMBERS', r'\d+'),
    ('ignore_NEWLINE', r'\s+'),
    ('ignore_COMMENT', r';[^\n]*'),
])


tokens = [
    'PARANTHESIS_OPENED',
    'PARANTHESIS_CLOSED',
    'PLAIN_TEXT',
    'NUMBERS',
    'ignore_NEWLINE',
    'ignore_COMMENT',
]

parser = ox.make_parser([
    ('atom : PLAIN_TEXT', lambda x: x),
    ('atom : NUMBERS', lambda x: x),
    ('expr : atom expr', lambda x, y: (x,) + y),
    ('expr : atom', lambda x: (x,)),
    ('block : PARANTHESIS_OPENED PARANTHESIS_CLOSED', lambda x, y: '()'),
    ('block : PARANTHESIS_OPENED expr PARANTHESIS_CLOSED', lambda x, y, z: y),
    ('atom : block', lambda x: x),
], tokens)



@click.command()
@click.argument('lisp_file', type=click.File('r'))
def printTree(lisp_file):
    
    tokens = lexer(lisp_file.read())
    pprint.pprint(parser(tokens))

printTree()

