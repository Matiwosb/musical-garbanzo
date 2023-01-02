from parsimonious.grammar import Grammar

grammar = """
    Expression      = second (Add / Sub)*
    Add      = "+" second
    Sub      = "-" second

    second   = first (Mul / Div)*
    Mul      = "*" first
    Div      = "/" first

    first   = Number

    Number      = ~"[0-9]+"

"""

parser = Grammar(grammar)


def string(tree):
    if tree.children:
        return ''.join([string(child) for child in tree])
    else:
        return tree.text


put = "8+7*9"

tree = parser.parse(put)

print(tree)

print(f'The result is {eval(string(tree))}')
