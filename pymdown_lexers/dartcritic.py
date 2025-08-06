from pygments.lexers import DartLexer
from pygments.lexer import bygroups
from pygments.token import *

class DartCriticLexer(DartLexer):
    name = 'DartCriticLexer'
    aliases = ['dart-critic']

    tokens = DartLexer.tokens.copy()
    # Modify the tokens dictionary here
    tokens['root'].insert(1, (r'//#\s*(.*?)(\n)', bygroups(Text, Whitespace)))
